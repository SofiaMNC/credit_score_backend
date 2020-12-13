import connexion
import six
from flask import abort

from swagger_server.models.installment_information import InstallmentInformation  # noqa: E501
from swagger_server.models.multiple_installment_information import MultipleInstallmentInformation  # noqa: E501
from swagger_server import util

from swagger_server.controllers import SAVED_INSTALLMENTS_DATA

def get_client_installment_info(client_id):  # noqa: E501
    """Get a client&#x27;s installment information by ID

    Returns a single client&#x27;s installment information # noqa: E501

    :param client_id: ID of client
    :type client_id: int

    :rtype: InstallmentInformation
    """

    if not isinstance(client_id, int):
        abort(400, "Supplied ID is not an integer")

    if client_id not in SAVED_INSTALLMENTS_DATA["SK_ID_CURR"].values:
        abort(404, "Client not found")


    return SAVED_INSTALLMENTS_DATA[SAVED_INSTALLMENTS_DATA["SK_ID_CURR"]==client_id].to_json(orient="records")


def get_clients_installment_info():  # noqa: E501
    """Get all clients&#x27; installment information

    Returns installments information for all clients # noqa: E501


    :rtype: MultipleInstallmentInformation
    """
    return SAVED_INSTALLMENTS_DATA.to_json(orient="records")
