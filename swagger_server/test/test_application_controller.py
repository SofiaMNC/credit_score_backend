# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.application_information import ApplicationInformation  # noqa: E501
from swagger_server.models.multiple_application_information import MultipleApplicationInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApplicationController(BaseTestCase):
    """ApplicationController integration test stubs"""

    def test_get_client_app_info(self):
        """Test case for get_client_app_info

        Get a client's banking information by ID
        """
        response = self.client.open(
            '/v2/application/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_app_info(self):
        """Test case for get_clients_app_info

        Get all clients' banking information
        """
        response = self.client.open(
            '/v2/applications',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
