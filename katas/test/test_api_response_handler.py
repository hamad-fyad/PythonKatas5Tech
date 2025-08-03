import unittest
from katas.api_response_handler import extract_user_data


class Test_api_response_handler(unittest.TestCase):
    def test_extract_user_data(self):
        sample_response = '''
        {
          "users": [
            {
              "id": "1",
              "name": "John Doe",
              "email": "john@example.com",
              "company": {
                "name": "Tech Corp",
                "website": "techcorp.com"
              },
              "address": {
                "city": "New York",
                "zipcode": "10001"
              }
            },
            {
              "id": "2",
              "name": "Jane Smith",
              "email": "jane@company.org",
              "company": {
                "name": "Innovation Ltd"
              },
              "address": {
                "city": "San Francisco"
              }
            }
          ]
        }
        '''
        expected_output = [
            {'id': '1', 'name': 'John Doe', 'email': 'john@example.com', 'company_name': 'Tech Corp', 'city': 'New York'},
            {'id': '2', 'name': 'Jane Smith', 'email': 'jane@company.org', 'company_name': 'Innovation Ltd', 'city': 'San Francisco'}
        ]
        result = extract_user_data(sample_response)
        self.assertEqual(result, expected_output)
    def test_extract_user_data_invalid_json(self):
        sample_response = 'Invalid JSON'
        with self.assertRaises(ValueError):
            extract_user_data(sample_response)