# -----------------------------------------------------------------------------------
# File   :   label_detector_controller.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------
from fastapi import APIRouter, Depends

from models.label_detector_model import LabelDetectorModel
from services.image_analyzer.aws_rekognition_service import AwsRekognitionService

router = APIRouter()


@router.post("/analyze")
async def analyze(input_data: LabelDetectorModel, rekognition: AwsRekognitionService = Depends()):
    return await rekognition.analyze(input_data)
