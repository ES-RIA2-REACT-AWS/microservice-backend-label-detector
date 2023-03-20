import unittest
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
        # when
        # then
        pass
