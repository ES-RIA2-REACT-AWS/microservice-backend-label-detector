# -----------------------------------------------------------------------------------
# File   :   image_downloader.py
# Author :   Mélodie Ohan
# Version:   21-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import httpx
from fastapi import status

from services.image_downloader.errors.image_downloader_errors import ImageDownloaderError


class ImageDownloader:
    @staticmethod
    async def download(image_url: str) -> bytes:
        async with httpx.AsyncClient() as client:
            response = await client.get(image_url)
            content_type = response.headers.get('Content-Type')
        if response.status_code != status.HTTP_200_OK and 'image' not in content_type:
            raise ImageDownloaderError
        return bytes(response.content)
