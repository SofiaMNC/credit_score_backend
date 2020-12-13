import connexion
import six
from flask import abort

from swagger_server import util

from swagger_server.controllers import SAVED_APP_DATA, SAVED_BUREAU_DATA, SAVED_BUREAU_BALANCE_DATA, \
                                       SAVED_CASH_DATA, SAVED_CARD_DATA, SAVED_INSTALLMENTS_DATA, SAVED_PREV_APP_DATA

from swagger_server.controllers import MODEL

def self_check():  # noqa: E501
    """Checks that the service is fully functional

    For valid response try integer IDs with value &gt;&#x3D; 1 and &lt;&#x3D; 10. # noqa: E501


    :rtype: None
    """
    response_msg = ""

    ## Check that the data used for training is available for display
    res = tuple(map(lambda a, b, c, d, e, f, g : a + b + c + d + e + f, 
                    SAVED_APP_DATA.shape, SAVED_BUREAU_DATA.shape, SAVED_BUREAU_BALANCE_DATA.shape, 
                    SAVED_CASH_DATA.shape, SAVED_CARD_DATA.shape, SAVED_INSTALLMENTS_DATA.shape, 
                    SAVED_PREV_APP_DATA.shape))
    
    if res[0] != 0 and res[1] != 0 and MODEL != None:
        response_msg = "🟢 Training data available to browse.\n🟢 Model available for predictions.\n✅ All systems go!"
    else:
        error_msg = ""

        if res[0] != 0 and res[1] != 0:
            error_msg = "🔴 Training data not available to browse.\n"
        if MODEL != None:
            error_msg += "🔴 Model unavailable for predictions.\n"

        error_msg += "🚨 Systems are no go!\nContact your sysadmin \nif the problem persists."
        abort(503, error_msg)  

    return response_msg


def train_model(body):  # noqa: E501
    """Trains the model on new data

    The model will be trained on the new data provided. BEWARE : This operation might take a few minutes # noqa: E501

    :param body: Train model on new data at URL given
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
