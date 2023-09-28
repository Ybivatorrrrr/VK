from unittest.mock import Mock, patch
from Task1 import SomeModel, predict_message_mood
import unittest


class TestPredictMessageMoodWithMock(unittest.TestCase):
    def test_good_message_with_mock(self):
        with patch.object(SomeModel, 'predict', return_value=0.9):
            model = SomeModel()
            result = predict_message_mood("Любое сообщение", model)
            self.assertEqual(result, "отл")

    def test_bad_message_with_mock(self):
        with patch.object(SomeModel, 'predict', return_value=0.2):
            model = SomeModel()
            result = predict_message_mood("Любое сообщение", model)
            self.assertEqual(result, "неуд")

    def test_neutral_message_with_mock(self):
        with patch.object(SomeModel, 'predict', return_value=0.5):
            model = SomeModel()
            result = predict_message_mood("Любое сообщение", model)
            self.assertEqual(result, "норм")


if __name__ == '__main__':
    unittest.main()
