# -----------------------------------------------------------------------------------
# File   :   aws_rekognition_client_error.py
# Author :   Mélodie Ohan
# Version:   21-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from services.image_analyzer.errors.aws_rekognition_error import AwsRekognitionError


class AwsRekognitionClientError(AwsRekognitionError):
    pass
