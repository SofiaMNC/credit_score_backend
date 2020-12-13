# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bureau_information import BureauInformation  # noqa: E501
from swagger_server.models.multiple_bureau_information import MultipleBureauInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBureauController(BaseTestCase):
    """BureauController integration test stubs"""

    def test_get_client_bureau_info(self):
        """Test case for get_client_bureau_info

        Get a client's bureau information by ID
        """
        response = self.client.open(
            '/v2/bureau/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_bureau_info(self):
        """Test case for get_clients_bureau_info

        Get all clients' bureau information
        """
        response = self.client.open(
            '/v2/bureau',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
