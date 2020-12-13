# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.card_information import CardInformation  # noqa: E501
from swagger_server.models.multiple_card_information import MultipleCardInformation  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCardController(BaseTestCase):
    """CardController integration test stubs"""

    def test_get_client_card_info(self):
        """Test case for get_client_card_info

        Get a client's card information by ID
        """
        response = self.client.open(
            '/v2/card/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_card_info(self):
        """Test case for get_clients_card_info

        Get all clients' card information
        """
        response = self.client.open(
            '/v2/card',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
