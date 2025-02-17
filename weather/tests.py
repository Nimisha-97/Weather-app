from api import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_api(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
