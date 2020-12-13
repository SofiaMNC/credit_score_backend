import connexion
import six
from flask import abort

from swagger_server.models.card_information import CardInformation  # noqa: E501
from swagger_server.models.multiple_card_information import MultipleCardInformation  # noqa: E501
from swagger_server import util

from swagger_server.controllers import SAVED_CARD_DATA

def get_client_card_info(client_id):  # noqa: E501
    """Get a client&#x27;s card information by ID

    Returns a single client&#x27;s card information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CardInformation
    """
    
    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_CARD_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    return SAVED_CARD_DATA[SAVED_CARD_DATA["SK_ID_CURR"]==client_id].to_json(orient="records")


def get_clients_card_info():  # noqa: E501
    """Get all clients&#x27; card information

    Returns card information for all clients # noqa: E501


    :rtype: MultipleCardInformation
    """
    return SAVED_CARD_DATA.to_json(orient="records")
