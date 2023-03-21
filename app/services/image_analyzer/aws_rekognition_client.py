# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_client.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from botocore.client import BaseClient
import boto3
from config.aws_credentials import AwsCredentials


class AwsRekognitionClient:
    """Provides clients from storage services"""

    _aws_credentials: AwsCredentials
    _aws_client: BaseClient

    def __init__(self):
        """Constructor
        """
        self._aws_credentials = AwsCredentials()
        self._aws_client = boto3.client('rekognition', region_name=self._aws_credentials.region_name,
                                        aws_access_key_id=self._aws_credentials.access_key_id,
                                        aws_secret_access_key=self._aws_credentials.secret_access_key)

    def __del__(self):
        self._aws_client.close()

    def get_aws_client(self) -> BaseClient:
        """Returns the aws config

        :return: BaseClient
        """
        return self._aws_client
