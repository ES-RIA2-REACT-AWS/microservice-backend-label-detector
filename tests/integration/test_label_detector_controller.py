import unittest
import json
from fastapi.testclient import TestClient
from main import app
from models.label_detector_model import LabelDetectorModel


class TestLabelDetectorController(unittest.TestCase):

    # Before all
    @classmethod
    def setUpClass(cls):
        pass

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

    def test_analyze_nominal_case_returns_labels(self):
        # given
        input_data = LabelDetectorModel(
            image_url="https://i.natgeofe.com/n/874df281-d3e0-489a-98c0-6b840023b828/newyork_NationalGeographic_2328428_16x9.jpg",
            max_label=10,
            min_confidence_level=0.5
        )

        # when
        response = self.client.post("/analyze", json=input_data.dict())

        # then
        self.assertEqual(response.status_code, 200)
