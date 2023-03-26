# -----------------------------------------------------------------------------------
# File   :   image_analyzer_service.py
# Author :   Mélodie Ohan
# Version:   22-03-2022 - original (dedicated to BI1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from models.label_detector_model import LabelDetectorModel


class ImageAnalyzerService:
    """ImageAnalyzerService

        All methods must be implemented in inheriting class.

        Notes
        ---
        This class works as an interface.
        There is no explicit interface implementation, no keyword interface in the current Python version.
        In order to "implement" ImageAnalyzerService, make your data object inherit from this class.
    """

    async def analyze(self, input_data: LabelDetectorModel) -> dict:
        """
        Submits the analysis of a given image to an AI
        :return: analysis result
        """
        raise NotImplementedError
