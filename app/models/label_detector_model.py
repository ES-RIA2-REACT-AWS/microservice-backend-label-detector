# -----------------------------------------------------------------------------------
# File   :   label_detector_model.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from pydantic import BaseModel, validator


class LabelDetectorModel(BaseModel):
    image_url: str
    max_label: int
    min_confidence_level: float

    @validator('image_url')
    def validate_image_url(cls, value: str):
        if not value:
            raise ValueError
        return value

    @validator('max_label')
    def validate_max_label(cls, value: int):
        if value <= 0:
            raise ValueError
        return value

    @validator('min_confidence_level')
    def validate_min_confidence_level(cls, value: float):
        if value < 0 or value > 1:
            raise ValueError
        return value
