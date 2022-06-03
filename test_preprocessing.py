from data_processing import preProcessing
import unittest


class TestStringMethods(unittest.TestCase):
    # local testing
    def test_preprocessing(self):
        self.assertEqual(preProcessing('/data', '/data'), "pre_processing")


if __name__ == "__main__":
    unittest.main()
