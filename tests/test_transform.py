import pytest
from dags.transform import transform_books_data


def test_transform_books_data():
    # Mock raw data
    raw_data = [
        {
            'title': 'Test Book 1',
            'author': 'Author 1',
            'published_date': 2023,
            'isbn': '1234567890',
            'source': 'OpenLibrary'
        },
        {
            'title': 'Test Book 2',
            'author': 'Author 2',
            'published_date': 2022,
            'isbn': '0987654321',
            'source': 'GoogleBooks'
        },
        {
            'title': 'Test Book 1',  # Duplicate based on title and author
            'author': 'Author 1',
            'published_date': 2023,
            'isbn': '1234567890',
            'source': 'OpenLibrary'

        },
        {
            'title': '',  # Invalid due to missing title
            'author': 'Author 3',
            'published_date': 2020,
            'isbn': '1111111111',
            'source': 'GoogleBooks'
        },
        {
            'title': 'Test Book 3',
            'author': '',  # Invalid due to missing author
            'published_date': 2021,
            'isbn': '2222222222',
            'source': 'OpenLibrary'
        }
    ]

    # Expected transformed data
    expected_result = [
        {
            'title': 'Test Book 1',
            'author': 'Author 1',
            'published_date': 2023,
            'isbn': '1234567890',
            'source': 'OpenLibrary'
        },
        {
            'title': 'Test Book 2',
            'author': 'Author 2',
            'published_date': 2022,
            'isbn': '0987654321',
            'source': 'GoogleBooks'
        }
    ]

    # Call the function
    result = transform_books_data(raw_data)

    # Assert that the result matches the expected result
    assert result == expected_result
