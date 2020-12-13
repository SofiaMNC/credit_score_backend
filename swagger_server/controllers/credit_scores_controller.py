import connexion
import six
from flask import abort

from swagger_server.models.credit_score import CreditScore  # noqa: E501
from swagger_server.models.credit_scores import CreditScores  # noqa: E501
from swagger_server import util

from swagger_server.controllers import CREDIT_SCORE_DATA

def get_client_credit_score(client_id):  # noqa: E501
    """Get credit score of a client by ID

    Returns a single credit score # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CreditScore
    """

    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in CREDIT_SCORE_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    return CREDIT_SCORE_DATA[CREDIT_SCORE_DATA["SK_ID_CURR"]==client_id].to_json(orient="records")


def get_clients_credit_score():  # noqa: E501
    """Get the credit scores of all clients

    Returns all clients&#x27; credit score # noqa: E501


    :rtype: CreditScores
    """
    return CREDIT_SCORE_DATA.to_json(orient="records")
