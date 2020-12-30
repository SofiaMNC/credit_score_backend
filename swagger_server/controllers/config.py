import numpy as np
import pandas as pd
from joblib import load
import requests
import io


#---------------------- Functions ----------------------#
def convert_types(df, print_info = False):
    
    original_memory = df.memory_usage().sum()
    
    # Iterate through each column
    for c in df:
        
        # Convert ids and booleans to integers
        if ('SK_ID' in c):
            df[c] = df[c].fillna(0).astype(np.int32)
            
        # Convert objects to category
        elif (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')
        
        # Booleans mapped to integers
        elif list(df[c].unique()) == [1, 0]:
            df[c] = df[c].astype(bool)
        
        # Float64 to float32
        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)
            
        # Int64 to int32
        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)
        
    new_memory = df.memory_usage().sum()
    
    if print_info:
        print(f'Original Memory Usage: {round(original_memory / 1e9, 2)} gb.')
        print(f'New Memory Usage: {round(new_memory / 1e9, 2)} gb.')
        
    return df

def download_csv_to_pd(url):
    '''
        Download a .csv file from a location at URL
        and transforms it into a pandas df
    '''
    urlData = requests.get(url).content
    rawData = pd.read_csv(io.StringIO(urlData.decode('utf-8')), sep=",")
    rawData = rawData.drop(rawData.columns[0], axis=1)

    return convert_types(rawData)

#---------------------- Variables ----------------------#

SAVED_DATA_BUCKET_URL = 'https://scoringapp.s3.eu-west-3.amazonaws.com/saved_data/'

datadir = "swagger_server/data/"
saved_datadir = "swagger_server/data/saved_data/"

#-------------------------------------------------------#

# Loading the original data that has been transformed and used to train
# the model on.

print("Loading training data into dataframes...")

SAVED_APP_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"application_test.csv")

SAVED_BUREAU_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"bureau_test.csv")

SAVED_BUREAU_BALANCE_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"bureau_balance_test.csv")

SAVED_CASH_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"cash_test.csv")

SAVED_CARD_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"card_test.csv")

SAVED_INSTALLMENTS_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"installments_test.csv")

SAVED_PREV_APP_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"prev_app_test.csv")

CREDIT_SCORE_DATA = download_csv_to_pd(SAVED_DATA_BUCKET_URL+"predictions_test.csv")

print("Training data loaded.")

# Loading the model 

print("Loading model...")

MODEL = load(datadir+"lgbm_trained_model_whole_dataset.joblib")

print("Model loaded.")

