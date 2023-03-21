import unittest

from services.image_analyzer.aws_rekognition_client import AwsRekognitionClient


class TestAwsRekognitionClient(unittest.TestCase):

    _client: AwsRekognitionClient

    def test_get_client_success(self):
        # given
        self._client = AwsRekognitionClient()

        # when
        aws_client = self._client.get_aws_client()

        # then
        self.assertIsNotNone(aws_client)
