import unittest
from unittest.mock import patch, MagicMock

# Import the T212 class from trading212_py/t212.py
# from trading212_py.t212 import T212
from trading212_py.t212 import T212

class TestT212(unittest.TestCase):

    @patch('trading212_py.t212.getenv')  # Mock the getenv function
    @patch('trading212_py.t212.requests.get')  # Mock the requests.get method
    def test_get_account_details(self, mock_get, mock_getenv):
        # Set up the mock environment variable
        mock_getenv.return_value = 'dummy_api_key'
        
        # Create a mock response object with expected data
        mock_response = MagicMock()
        expected_account_details = {'account_id': '123', 'balance': 1000.0}
        mock_response.json.return_value = expected_account_details
        mock_get.return_value = mock_response
        
        # Initialize the T212 class and call the get_account_details method
        t212 = T212()
        result = t212.get_account_details()

        # Assertions
        self.assertEqual(result, expected_account_details)
        mock_get.assert_called_once_with(
            url="https://api.t212.com/v1/account/details",
            headers={
                'Authorization': 'Bearer dummy_api_key',
                'Content-Type': 'application/json'
            }
        )

    @patch('trading212_py.t212.getenv')  # Mock the getenv function
    @patch('trading212_py.t212.requests.get')  # Mock the requests.get method
    def test_get_instruments(self, mock_get, mock_getenv):
        # Set up the mock environment variable
        mock_getenv.return_value = 'dummy_api_key'
        
        # Create a mock response object with expected data
        mock_response = MagicMock()
        expected_instruments = [
            {'instrument_id': '1', 'name': 'Instrument 1'},
            {'instrument_id': '2', 'name': 'Instrument 2'}
        ]
        mock_response.json.return_value = expected_instruments
        mock_get.return_value = mock_response
        
        # Initialize the T212 class and call the get_instruments method
        t212 = T212()
        result = t212.get_instruments()

        # Assertions
        self.assertEqual(result, expected_instruments)
        mock_get.assert_called_once_with(
            url="https://api.t212.com/v1/instruments",
            headers={
                'Authorization': 'Bearer dummy_api_key',
                'Content-Type': 'application/json'
            }
        )

if __name__ == '__main__':
    unittest.main()
