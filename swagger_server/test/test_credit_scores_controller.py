# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.credit_score import CreditScore  # noqa: E501
from swagger_server.models.credit_scores import CreditScores  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCreditScoresController(BaseTestCase):
    """CreditScoresController integration test stubs"""

    def test_get_client_credit_score(self):
        """Test case for get_client_credit_score

        Get credit score of a client by ID
        """
        response = self.client.open(
            '/v2/credit_score/{clientId}'.format(client_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_clients_credit_score(self):
        """Test case for get_clients_credit_score

        Get the credit scores of all clients
        """
        response = self.client.open(
            '/v2/credit_scores',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
