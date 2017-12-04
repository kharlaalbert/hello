import unittest
import app
from app import hello, app

class SimpleTest(unittest.TestCase):
    def setUp(self):
	    self.app = app.test_client()
	    self.app.testing = True
    def test_status_code(self):
	    result = self.app.get('/')
	    self.assertEqual(result.status_code,200)
    def test_data_displayed(self):
	    result = self.app.get('/')
	    self.assertTrue('Hello World' in result.get_data(as_text=True))
	    self.assertTrue('by Kharla Parnada' in result.get_data(as_text=True))
	    self.assertTrue('Nothing' in result.get_data(as_text=True))
    
if __name__ == '__main__':
	unittest.main()

