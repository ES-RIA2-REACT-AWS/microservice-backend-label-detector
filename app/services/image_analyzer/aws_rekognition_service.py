# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import requests
import json

from services.image_analyzer.aws_rekognition_client import AwsRekognitionClient
from services.image_analyzer.image_analyzer_service import ImageAnalyzerService
from services.image_analyzer.errors.aws_rekognition_download_failed_error import AwsRekognitionDownloadFailedError


class AwsRekognitionService(ImageAnalyzerService):
    _client: AwsRekognitionClient

    async def analyze(self, image_url: str, max_label: int, min_confidence_level: float) -> json:
        self._client = AwsRekognitionClient()
        image = self._download_image(image_url)
        response = self._client.get_aws_client().detect_labels(
            Image={'Bytes': image},
            MaxLabels=max_label,
            MinConfidence=min_confidence_level
        )
        return AwsRekognitionService._format_output(response)

    def _download_image(self, image_url: str) -> bytes:
        response = requests.get(image_url)
        if response.status_code != 200:
            raise AwsRekognitionDownloadFailedError
        return response.content

    @staticmethod
    def _format_output(json_input: json) -> json:
        formatted_output = {}
        if not json_input['Labels']:
            raise Exception
        formatted_output["labels"] = {}
        for i, label in enumerate(json_input['Labels']):
            formatted_output['labels'][i] = {'name': label['Name'], 'confidence': label['Confidence']}
        return json.dumps(formatted_output)
