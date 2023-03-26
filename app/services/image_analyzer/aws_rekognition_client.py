# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_client.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import boto3
from os import getenv
from botocore.client import BaseClient
from boto3.exceptions import Boto3Error


class AwsRekognitionClient:
    """Provides clients from storage services"""

    _aws_client: BaseClient

    def __init__(self):
        """Constructor
        """
        try:
            self._aws_client = boto3.client('rekognition', region_name=getenv("AWS_REGION_NAME"),
                                            aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                                            aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"))
        except Boto3Error:
            raise AwsRekognitionClient("Cannot connect to image analysis service.")

    def __del__(self):
        self._aws_client.close()

    def get_aws_client(self) -> BaseClient:
        """Returns the aws config

        :return: BaseClient
        """
        return self._aws_client
