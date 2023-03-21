# -----------------------------------------------------------------------------------
# File   :   image_analyzer_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

class ImageAnalyzerService:
    """ImageAnalyzerService

        All methods must be implemented in inheriting class.

        Notes
        ---
        This class works as an interface.
        There is no explicit interface implementation, no keyword interface in the current Python version.
        In order to "implement" ImageAnalyzerService, make your data object inherit from this class.
    """

    async def analyze(self, image_url: str, max_label: int, min_confidence_level: float) -> dict:
        """
        Analyze an image from an url according to the max_label and min_confidence_level parameters
        :param image_url: str
        :param max_label: int
        :param min_confidence_level: float
        :return: analysis result
        """
        raise NotImplementedError

    def _download_image(self, image_url: str) -> bytes:
        raise NotImplementedError
