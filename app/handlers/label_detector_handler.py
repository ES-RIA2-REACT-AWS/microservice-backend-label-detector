from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from controllers.label_detector_controller import router as label_detector_router

from services.image_analyzer.errors.aws_rekognition_error import AwsRekognitionError
from services.image_analyzer.errors.aws_rekognition_client_error import AwsRekognitionClientError
from services.image_analyzer.errors.aws_rekognition_download_failed_error import AwsRekognitionDownloadFailedError
from config.errors.credentials_missing_config_value_error import CredentialsMissingConfigValueError
from config.errors.credentials_config_file_not_found_error import CredentialsConfigFileNotFoundError


app = FastAPI()
app.include_router(label_detector_router)


@app.exception_handler(CredentialsMissingConfigValueError)
async def credentials_missing_config_value_error_handler(request: Request, exc: CredentialsMissingConfigValueError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Unprocessable Content"},
    )


@app.exception_handler(AwsRekognitionError)
async def aws_rekognition_error_handler(request: Request, exc: AwsRekognitionError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Unprocessable Content"},
    )


@app.exception_handler(AwsRekognitionDownloadFailedError)
async def aws_rekognition_download_failed_error_handler(request: Request, exc: AwsRekognitionDownloadFailedError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Unprocessable Content"},
    )


@app.exception_handler(CredentialsConfigFileNotFoundError)
async def credentials_config_file_not_found_error_handler(request: Request, exc: CredentialsConfigFileNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error"},
    )


@app.exception_handler(AwsRekognitionClientError)
async def aws_rekognition_client_error_handler(request: Request, exc: AwsRekognitionClientError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal Server Error"},
    )


def add_label_detector_handlers(main_app: FastAPI):
    main_app.add_exception_handler(CredentialsMissingConfigValueError, credentials_missing_config_value_error_handler)
    main_app.add_exception_handler(AwsRekognitionError, aws_rekognition_error_handler)
    main_app.add_exception_handler(AwsRekognitionDownloadFailedError, aws_rekognition_download_failed_error_handler)
    main_app.add_exception_handler(CredentialsConfigFileNotFoundError, credentials_config_file_not_found_error_handler)
    main_app.add_exception_handler(AwsRekognitionClientError, aws_rekognition_client_error_handler)
