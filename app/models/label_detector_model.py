# -----------------------------------------------------------------------------------
# File   :   label_detector_model.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from pydantic import BaseModel, validator, HttpUrl, Field


class LabelDetectorModel(BaseModel):

    image_url: HttpUrl = Field(...)
    max_label: int = Field(10, ge=1, le=100)
    min_confidence_level: float = Field(0.7, ge=0.0, le=1.0)

    class Config:
        """LabelDetectorModel validator rules"""
        extra = 'forbid'
        allow_mutation = False
        validate_all = True

    @validator('image_url')
    def validate_image_url(cls, value: HttpUrl):
        return value

    @validator('max_label')
    def validate_max_label(cls, value: int):
        return value

    @validator('min_confidence_level')
    def validate_min_confidence_level(cls, value: float):
        return value
