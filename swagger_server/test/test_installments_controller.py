# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.installment_information import InstallmentInformation  # noqa: E501
from swagger_server.models.multiple_installment_information import MultipleInstallmentInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstallmentsController(BaseTestCase):
    """InstallmentsController integration test stubs"""

    def test_get_client_installment_info(self):
        """Test case for get_client_installment_info

        Get a client's installment information by ID
        """
        response = self.client.open(
            '/v2/installment/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_installment_info(self):
        """Test case for get_clients_installment_info

        Get all clients' installment information
        """
        response = self.client.open(
            '/v2/installments',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
