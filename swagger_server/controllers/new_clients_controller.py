import connexion
import six

from swagger_server.models.credit_scores import CreditScores  # noqa: E501
from swagger_server import util


def new_clients(body):  # noqa: E501
    """Integrate new clients

    Integrates new clients&#x27; info in the database, and predicts their credit score # noqa: E501

    :param body: Integrates new clients&#x27; info in the database, and predicts their credit score
    :type body: dict | bytes

    :rtype: CreditScores
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501

        print(body)

        # Load the data and give to the transform function

        # predict 

        # Add to the saved data

    return 'do some magic!'
