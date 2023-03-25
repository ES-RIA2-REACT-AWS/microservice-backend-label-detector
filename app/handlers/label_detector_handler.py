# -----------------------------------------------------------------------------------
# File   :   label_detector_handler.py
# Author :   Mélodie Ohan
# Version:   21-03-2023 - original (dedicated to RIA1)
# Remarks:   This file defines which server status code will be returned according to
#            the exception categories.
# -----------------------------------------------------------------------------------

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from controllers.label_detector_controller import router as label_detector_router

from config.errors.credentials_error import CredentialsError
from services.image_analyzer.errors.aws_rekognition_service_image_error import AwsRekognitionServiceImageError
from services.image_analyzer.errors.aws_rekognition_client_error import AwsRekognitionClientError
from services.image_analyzer.errors.aws_rekognition_service_error import AwsRekognitionServiceError

app = FastAPI()
app.include_router(label_detector_router)


# ------------------------------  STATUS_CODE 5XX  -------------------------------

@app.exception_handler(CredentialsError)
async def credentials_error_handler(request: Request, exc: CredentialsError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Incorrect server configuration"},
    )


@app.exception_handler(AwsRekognitionServiceError)
async def aws_rekognition_service_error_handler(request: Request, exc: AwsRekognitionServiceError):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"message": "Unable to perform image analysis"},
    )


@app.exception_handler(AwsRekognitionClientError)
async def aws_rekognition_client_error_handler(request: Request, exc: AwsRekognitionClientError):
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={"message": "Unable to access the service client"},
    )


# ------------------------------  STATUS_CODE 4XX  -------------------------------

@app.exception_handler(AwsRekognitionServiceImageError)
async def aws_rekognition_service_image_error_handler(request: Request, exc: AwsRekognitionServiceImageError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": "Cannot extract the image from the provided url."},
    )


def add_label_detector_handlers(main_app: FastAPI):
    main_app.add_exception_handler(CredentialsError, credentials_error_handler)
    main_app.add_exception_handler(AwsRekognitionServiceError, aws_rekognition_service_error_handler)
    main_app.add_exception_handler(AwsRekognitionClientError, aws_rekognition_client_error_handler)
    main_app.add_exception_handler(AwsRekognitionServiceImageError, aws_rekognition_service_image_error_handler)

