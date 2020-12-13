import connexion
import six
from flask import abort

from swagger_server.models.multiple_previous_application_information import MultiplePreviousApplicationInformation  # noqa: E501
from swagger_server.models.previous_application_information import PreviousApplicationInformation  # noqa: E501
from swagger_server import util

from swagger_server.controllers import SAVED_PREV_APP_DATA

def get_client_previous_app_info(client_id):  # noqa: E501
    """Get a client&#x27;s banking information by ID

    Returns a single client&#x27;s previous application information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: PreviousApplicationInformation
    """

    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_PREV_APP_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    return SAVED_PREV_APP_DATA[SAVED_PREV_APP_DATA["SK_ID_CURR"]==client_id].to_json(orient="records")


def get_clients_previous_app_info():  # noqa: E501
    """Get all clients&#x27; bureau information

    Returns previous application information for all clients # noqa: E501


    :rtype: MultiplePreviousApplicationInformation
    """
    return SAVED_PREV_APP_DATA.to_json(orient="records")
