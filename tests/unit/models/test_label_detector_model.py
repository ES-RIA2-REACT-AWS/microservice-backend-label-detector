import unittest
from models.label_detector_model import LabelDetectorModel
from pydantic import ValidationError


class TestLabelDetectorModel(unittest.TestCase):

    _default_nb_label: int = 10
    _default_confidence: float = 0.7

    _image_url: str = "https://example.com/img.png"
    _max_label: int = 4
    _min_confidence_level: float = 0.8

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
        pass

    def test_constructor_nominal_case_success(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": self._max_label,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        ldm = LabelDetectorModel(**input_data)

        # then
        self.assertEqual(ldm.image_url, input_data["image_url"])
        self.assertEqual(ldm.max_label, input_data["max_label"])
        self.assertEqual(ldm.min_confidence_level, input_data["min_confidence_level"])

    def test_constructor_default_values_success(self):
        # given
        # refer to class attributes

        # when
        ldm = LabelDetectorModel(image_url=self._image_url)

        # then
        self.assertEqual(ldm.image_url, self._image_url)
        self.assertEqual(ldm.max_label, self._default_nb_label)
        self.assertEqual(ldm.min_confidence_level, self._default_confidence)

    def test_constructor_missing_image_url_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": None,
            "max_label": self._max_label,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_incorrect_image_url_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": "Lorem ipsum dolor sit amet..",
            "max_label": self._max_label,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_missing_max_label_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": None,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_incorrect_max_label_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": 1000,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_negative_max_label_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": -1,
            "min_confidence_level": self._min_confidence_level
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_missing_min_confidence_level_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": self._max_label,
            "min_confidence_level": None
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)

    def test_constructor_incorrect_min_confidence_level_raises_exception(self):
        # given
        input_data: dict = {
            "image_url": self._image_url,
            "max_label": self._max_label,
            "min_confidence_level": 150
        }

        # when
        # then
        with self.assertRaises(ValidationError):
            LabelDetectorModel(**input_data)
