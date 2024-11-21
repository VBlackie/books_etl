import pytest
from unittest.mock import patch
from dags.extract import extract_books_data


def test_extract_books_data():
    mock_response = {
        'docs': [
            {
                'title': 'Test Book',
                'author_name': ['Test Author'],
                'first_publish_year': 2023,
                'isbn': ['1234567890']
            }
        ]
    }
    with patch('dags.extract.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = extract_books_data()
        expected_result = [{
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': 2023,
            'isbn': '1234567890'
        }]

        assert result == expected_result
