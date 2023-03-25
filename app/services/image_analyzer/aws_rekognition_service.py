# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------


import json
import httpx
from fastapi import status
from botocore.exceptions import ClientError

from models.label_detector_model import LabelDetectorModel
from services.image_analyzer.aws_rekognition_client import AwsRekognitionClient
from services.image_analyzer.image_analyzer_service import ImageAnalyzerService
from services.image_analyzer.errors.aws_rekognition_service_error import AwsRekognitionServiceError
from services.image_analyzer.errors.aws_rekognition_service_image_error import AwsRekognitionServiceImageError


class AwsRekognitionService(ImageAnalyzerService):
    _client: AwsRekognitionClient

    async def analyze(self, input_data: LabelDetectorModel) -> json:
        self._client = AwsRekognitionClient()
        image: bytes = await AwsRekognitionService._convert_to_bytes(input_data.image_url)
        response: dict = await self._submit_to_aws_rekognition(image,
                                                               input_data.max_label,
                                                               input_data.min_confidence_level)
        return AwsRekognitionService._format_output(response)

    async def _submit_to_aws_rekognition(self, image: bytes, max_label: int, min_confidence_level: float) -> dict:
        try:
            response = self._client.get_aws_client().detect_labels(
                Image={'Bytes': image},
                MaxLabels=max_label,
                MinConfidence=min_confidence_level*100.
            )
        except ClientError as e:
            raise AwsRekognitionServiceError(str(e))
        return response

    @staticmethod
    async def _convert_to_bytes(image_url: str) -> bytes:
        """Downloads the image data from image_url and returns its content as bytes
        :param image_url:
        :return: bytes
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(image_url)
            content_type = response.headers.get('Content-Type')
        if response.status_code != status.HTTP_200_OK and 'image' not in content_type:
            raise AwsRekognitionServiceImageError
        return bytes(response.content)

    @staticmethod
    def _format_output(json_input: dict) -> json:
        """Format the
        :param json_input:
        :return:
        """
        formatted_output = dict({})
        formatted_output["labels"] = []
        for label in json_input['Labels']:
            formatted_output['labels'].append({'name': label['Name'], 'confidence': label['Confidence']})
        return json.dumps(formatted_output)
