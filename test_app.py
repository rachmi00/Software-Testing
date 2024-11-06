import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')
        
        # Check the status code of the response
        self.assertEqual(response.status_code, 200)
        
        # Check the response data
        self.assertEqual(response.get_json(), {"message": "Hello level 400 FET, Quality Assurance!"})

if __name__ == '__main__':
    unittest.main()
