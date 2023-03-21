import unittest

from services.client.client import Client


class TestClient(unittest.TestCase):

    _client: Client

    def test_get_client_success(self):
        # given
        self._client = Client()

        # when
        aws_client = self._client.get_aws_client()

        # then
        self.assertIsNotNone(aws_client)