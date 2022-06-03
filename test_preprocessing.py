from data_processing import preProcessing
import unittest

class TestStringMethods(unittest.TestCase):
    # local testing
    def test_preprocessing(self):
        self.assertEqual( preProcessing('/data', '/data'), "pre_processing")
        print( preProcessing('/data', '/data') )
    # def test_add():
    #     assert 1+1 == 2 '1+1 == 2 is right'

if __name__=="__main__":
    unittest.main()
