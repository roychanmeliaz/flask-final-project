from app import connex_app
import directors
import unittest

class FlaskTestCase(unittest.TestCase):
    # test the response code of the api
    def test_get_directors_response(self):
        connex_app.app.testing = True
        tester = connex_app.app.test_client(self)
        response = tester.get('/api/directors')
        self.assertEqual(response.status_code,200)
    
    # test the response type of the api
    def test_get_directors_type(self):
        self.assertIs(type(directors.read_all()),list)

if __name__ == '__main__':
    unittest.main()