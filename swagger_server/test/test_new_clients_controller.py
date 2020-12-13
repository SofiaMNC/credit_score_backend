# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.credit_scores import CreditScores  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNewClientsController(BaseTestCase):
    """NewClientsController integration test stubs"""

    def test_new_clients(self):
        """Test case for new_clients

        Integrate new clients
        """
        body = 'body_example'
        response = self.client.open(
            '/v2/clients',
            method='POST',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
