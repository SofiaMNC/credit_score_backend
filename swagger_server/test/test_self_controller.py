# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSelfController(BaseTestCase):
    """SelfController integration test stubs"""

    def test_self_check(self):
        """Test case for self_check

        Checks that the service is fully functional
        """
        response = self.client.open(
            '/v2/self_check',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_train_model(self):
        """Test case for train_model

        Trains the model on new data
        """
        body = 'body_example'
        response = self.client.open(
            '/v2/train_model',
            method='PUT',
            data=json.dumps(body),
            content_type='text/plain')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
