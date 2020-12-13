# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.multiple_previous_application_information import MultiplePreviousApplicationInformation  # noqa: E501
from swagger_server.models.previous_application_information import PreviousApplicationInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPreviousApplicationController(BaseTestCase):
    """PreviousApplicationController integration test stubs"""

    def test_get_client_previous_app_info(self):
        """Test case for get_client_previous_app_info

        Get a client's banking information by ID
        """
        response = self.client.open(
            '/v2/previous_application/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_previous_app_info(self):
        """Test case for get_clients_previous_app_info

        Get all clients' bureau information
        """
        response = self.client.open(
            '/v2/previous_applications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
