# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import requests

from services.image_analyzer.aws_rekognition_client import AwsRekognitionClient
from services.image_analyzer.image_analyzer_service import ImageAnalyzerService


class AwsRekognitionService(ImageAnalyzerService):
    _client: AwsRekognitionClient

    async def analyze(self, image_url: str, max_label: int, min_confidence_level: float) -> list:
        self._client = AwsRekognitionClient()
        image = self._download_image(image_url)
        response = self._client.get_aws_client().detect_labels(
            Image={'Bytes': image},
            MaxLabels=max_label,
            MinConfidence=min_confidence_level
        )
        labels = [{'name': label['Name'], 'confidence': label['Confidence']} for label in response['Labels']]
        return labels

    def _download_image(self, image_url: str) -> bytes:
        response = requests.get(image_url)
        return response.content
