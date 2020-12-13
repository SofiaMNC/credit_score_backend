# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bureau_balance_information import BureauBalanceInformation  # noqa: E501
from swagger_server.models.multiple_bureau_balance_information import MultipleBureauBalanceInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBureauBalanceController(BaseTestCase):
    """BureauBalanceController integration test stubs"""

    def test_get_client_bureau_balance_info(self):
        """Test case for get_client_bureau_balance_info

        Get a client's bureau balance information by ID
        """
        response = self.client.open(
            '/v2/bureau_balance/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_bureau_balance_info(self):
        """Test case for get_clients_bureau_balance_info

        Get all clients' bureau balance information
        """
        response = self.client.open(
            '/v2/bureau_balance',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
