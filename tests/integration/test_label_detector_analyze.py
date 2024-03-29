# -----------------------------------------------------------------------------------
# File   :   test_label_detector_analyze.py
# Author :   Mélodie Ohan
# Version:   24-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import unittest
from fastapi import Response
from fastapi.testclient import TestClient
from main import app


class TestLabelDetectorAnalyze(unittest.TestCase):
    _client: TestClient

    _image_url: str = "https://mir-s3-cdn-cf.behance.net/project_modules/fs/b907f993179931.5e5e5fc07af3d.jpg"

    _default_max_label: int = 10
    _default_min_confidence: float = 0.7

    # Before all
    @classmethod
    def setUpClass(cls):
        cls._client = TestClient(app)

    # After all
    @classmethod
    def tearDownClass(cls):
        pass

    # After each
    def tearDown(self):
        pass

    # Before each
    def setUp(self):
        self.client = TestClient(app)

    # ----------------- Helpers   ----------------- #
    @classmethod
    def _post(cls, route: str, data):
        """Use FastAPI TestClient post method to test our endpoint"""
        return cls._client.post(route,
                                headers={"X-Token": "coneofsilence", "Content-Type": "application/json"},
                                json=data)

    @staticmethod
    def _min_confidence_is_respected(response: Response, min_confidence: float) -> bool:
        response_dict = response.json()
        for label in response_dict['labels']:
            if float(label['confidence']) < min_confidence * 100.:
                return False
        return True

    @staticmethod
    def _max_label_is_respected(response: Response, max_label: int) -> bool:
        response_dict = response.json()
        return len(response_dict['labels']) <= max_label

    # ---------------------------------------------- #

    def test_analyze_nominal_case_returns_labels(self):
        # given
        data = {
            "image_url": self._image_url
        }

        # when
        response = TestLabelDetectorAnalyze._post("/analyze", data)

        # then
        self.assertTrue(self._max_label_is_respected(response, self._default_max_label))
        self.assertTrue(self._min_confidence_is_respected(response, self._default_min_confidence))

    def test_analyze_different_max_label_returns_labels(self):
        # given
        max_label: int = 15
        data = {
            "image_url": self._image_url,
            "max_label": max_label
        }

        # when
        response = TestLabelDetectorAnalyze._post("/analyze", data)

        # then
        self.assertTrue(self._max_label_is_respected(response, max_label))
        self.assertTrue(self._min_confidence_is_respected(response, self._default_min_confidence))

    def test_analyze_different_min_confidence_returns_labels(self):
        # given
        min_confidence: float = 0.4
        data = {
            "image_url": self._image_url,
            "min_confidence_level": min_confidence
        }

        # when
        response = TestLabelDetectorAnalyze._post("/analyze", data)

        # then
        self.assertTrue(self._max_label_is_respected(response, self._default_max_label))
        self.assertTrue(self._min_confidence_is_respected(response, min_confidence))

    def test_analyze_different_parameters_returns_labels(self):
        # given
        max_label: int = 4
        min_confidence: float = 0.4
        data = {
            "image_url": self._image_url,
            "min_confidence_level": min_confidence,
            "max_label": max_label
        }

        # when
        response = TestLabelDetectorAnalyze._post("/analyze", data)

        # then
        self.assertTrue(self._max_label_is_respected(response, max_label))
        self.assertTrue(self._min_confidence_is_respected(response, min_confidence))
