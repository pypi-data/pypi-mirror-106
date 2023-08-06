from pipeline_worker import convertToLaz, convertFromLaz, convertLazToEPTLaz, convertLAZTo2D
import unittest
import shutil
import os

class TestWorker(unittest.TestCase):
    def test_view(self):
        self.assertEqual(convertLazToEPTLaz("la.laz", "le", "la/untwine"), "la.laz does not exist.", "Should be la.laz does not exist.")
        self.assertFalse(os.path.exists("le/la.laz"))
        self.assertTrue("--files=" in convertLazToEPTLaz("./test_data/from/test.laz", "./test_data/to", "./untwine/build/untwine"))
        self.assertTrue(os.path.exists("./test_data/to/test"))
        shutil.rmtree("./test_data/to/test")

    def test_get(self):
        self.assertEqual(convertToLaz("la.ept", "le"), "la.ept does not exist.", "Should be la.ept does not exist.")
        self.assertFalse(os.path.exists("le/la.ept"))
        self.assertTrue("metadata" in convertToLaz("./test_data/from/test.laz", "./test_data/to"))
        self.assertTrue(os.path.exists("./test_data/to/test.laz"))
        os.remove("./test_data/to/test.laz") 

    def test_get2d(self):
        self.assertEqual(convertLAZTo2D("la.laz", "le"), "la.laz does not exist.", "Should be la.laz does not exist.")
        self.assertFalse(os.path.exists("le/la.tif"))
        self.assertTrue("metadata" in convertLAZTo2D("./test_data/from/test.laz", "./test_data/to"))
        self.assertTrue(os.path.exists("./test_data/to/test.tif"))
        os.remove("./test_data/to/test.tif") 

if __name__ == '__main__':
    unittest.main()


