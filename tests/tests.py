import unittest
import app
from app import hello, app

class SimpleTest(unittest.TestCase):
    def setUp(self):
	    self.app = app.test_client()
	    self.app.testing = True
    def test_status(self):
	    result = self.app.get('/')
	    self.assertEqual(result.status_code,200)
if __name__ == '__main__':
	unittest.main()

