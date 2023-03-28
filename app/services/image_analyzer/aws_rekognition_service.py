# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------


import httpx
from fastapi import status, Response
from botocore.exceptions import ClientError

from models.label_detector_model import LabelDetectorModel
from services.image_analyzer.aws_rekognition_client import AwsRekognitionClient
from services.image_analyzer.image_analyzer_service import ImageAnalyzerService
from services.image_analyzer.errors.aws_rekognition_service_error import AwsRekognitionServiceError
from services.image_analyzer.errors.aws_rekognition_service_image_error import AwsRekognitionServiceImageError


class AwsRekognitionService(ImageAnalyzerService):
    _client: AwsRekognitionClient

    def __init__(self):
        self._client = AwsRekognitionClient()

    async def analyze(self, input_data: LabelDetectorModel) -> dict:
        image: bytes = await AwsRekognitionService._convert_to_bytes(input_data.image_url)
        response: Response = await self._submit_to_aws_rekognition(image, input_data.max_label,
                                                                   input_data.min_confidence_level)
        return AwsRekognitionService._extract_labels(response)

    async def _submit_to_aws_rekognition(self, image: bytes, max_label: int, min_confidence_level: float) -> Response:
        try:
            response = self._client.get_aws_client().detect_labels(
                Image={'Bytes': image},
                MaxLabels=max_label,
                MinConfidence=min_confidence_level * 100.
            )
        except ClientError as e:
            raise AwsRekognitionServiceError(str(e))
        return response

    @staticmethod
    async def _convert_to_bytes(image_url: str) -> bytes:
        """Downloads the image data from image_url and returns its content as bytes
        :param image_url: str
        :return: bytes
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(image_url)
            content_type = response.headers.get('Content-Type')
        if response.status_code != status.HTTP_200_OK and 'image' not in content_type:
            raise AwsRekognitionServiceImageError
        return bytes(response.content)

    @staticmethod
    def _extract_labels(response: Response) -> dict:
        """
        Retrieves the labels from the server response
        :param response:
        :return dict
        """
        labels = dict({})
        labels["labels"] = []
        for label in response['Labels']:
            labels['labels'].append({'name': label['Name'], 'confidence': label['Confidence']})
        return labels
