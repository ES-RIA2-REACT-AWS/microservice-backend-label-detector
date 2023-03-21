# -----------------------------------------------------------------------------------
# File   :   label_detector_controller.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from fastapi import APIRouter, HTTPException

from models.label_detector_model import LabelDetectorModel
from services.image_analyzer.aws_rekognition_service import AwsRekognitionService
from services.image_analyzer.errors.aws_rekognition_error import AwsRekognitionError

router = APIRouter()


@router.post("/analyze")
async def analyze(input_data: LabelDetectorModel) -> dict:
    try:
        rekognition = AwsRekognitionService()
        results = await rekognition.analyze(input_data.image_url, input_data.max_label, input_data.min_confidence_level)
        return results
    except ConnectionError:
        raise HTTPException(status_code=500)
    except (ValueError, KeyError, TypeError, AwsRekognitionError):
        raise HTTPException(status_code=422)
