# -----------------------------------------------------------------------------------
# File   :   label_detector_controller.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from fastapi import APIRouter
from models.label_detector_model import LabelDetectorModel

router = APIRouter()


@router.post("/analyze")
async def analyze(input_data: LabelDetectorModel) -> dict:
    return {
        "Labels": [
            {
                "Name": "Animal",
                "Confidence": 0.9
            }
        ]
    }
