import os
import unittest
import json

from api import create_app


class ApiV1Test(unittest.TestCase):

    def setUp(self):
        app = create_app(os.getenv('FLASK_CONFIG', 'default'))
        app.testing = True
        self.app = app.test_client()

    def get_api_response(self, url):
        return json.loads(self.app.get(url).data.decode())

    def test_not_an_integer_error(self):
        response_str = self.get_api_response('/v1/fib/abc')
        response_float = self.get_api_response('/v1/fib/0.1')
        self.assertEqual(response_str.get('error'), 'Not an integer.')
        self.assertEqual(response_float.get('error'), 'Not an integer.')

    def test_out_of_range_error(self):
        response_neg = self.get_api_response('/v1/fib/-1')
        response_gt_1000 = self.get_api_response('/v1/fib/1001')
        self.assertEqual(response_neg.get('error'),
                         'The number should be in range from 0 to 1000.')
        self.assertEqual(response_gt_1000.get('error'),
                         'The number should be in range from 0 to 1000.')

    def test_valid_sequence(self):
        response_10 = self.get_api_response('/v1/fib/10')
        response_0 = self.get_api_response('/v1/fib/0')
        response_1 = self.get_api_response('/v1/fib/1')
        response_1000 = self.get_api_response('/v1/fib/1000')
        self.assertEqual(response_10.get('sequence'),
                         [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(response_0.get('sequence'), [0])
        self.assertEqual(response_1.get('sequence'), [0, 1])
        self.assertEqual(len(response_1000.get('sequence', [])), 1001)

    def test_invalid_call_error(self):
        response = self.get_api_response('/v1/fib/')
        response_1 = self.get_api_response('/v1/fib/123/abc')
        response_2 = self.get_api_response('/v1/')
        self.assertEqual(response.get('error'), 'Invalid API call.')
        self.assertEqual(response_1.get('error'), 'Invalid API call.')
        self.assertEqual(response_2.get('error'), 'Invalid API call.')


if __name__ == '__main__':
    unittest.main()
