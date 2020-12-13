import connexion
import six
from flask import abort

from swagger_server.models.cash_information import CashInformation  # noqa: E501
from swagger_server.models.multiple_cash_information import MultipleCashInformation  # noqa: E501
from swagger_server import util

from swagger_server.controllers import SAVED_CASH_DATA

def get_client_cash_info(client_id):  # noqa: E501
    """Get a client&#x27;s cash information by ID

    Returns a single client&#x27;s cash information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: CashInformation
    """

    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_CASH_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")

    return SAVED_CASH_DATA[SAVED_CASH_DATA["SK_ID_CURR"]==client_id].to_json(orient="records")


def get_clients_cash_info():  # noqa: E501
    """Get all clients&#x27; cash information

    Returns cash information for all clients # noqa: E501


    :rtype: MultipleCashInformation
    """
    return SAVED_CASH_DATA.to_json(orient="records")
