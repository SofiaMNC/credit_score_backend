# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cash_information import CashInformation  # noqa: E501
from swagger_server.models.multiple_cash_information import MultipleCashInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCashController(BaseTestCase):
    """CashController integration test stubs"""

    def test_get_client_cash_info(self):
        """Test case for get_client_cash_info

        Get a client's cash information by ID
        """
        response = self.client.open(
            '/v2/cash/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_cash_info(self):
        """Test case for get_clients_cash_info

        Get all clients' cash information
        """
        response = self.client.open(
            '/v2/cash',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
