import pytest
from dags.transform import transform_books_data


def test_transform_books_data():
    # Mock raw data
    raw_data = [
        {
            'title': 'Book With Full Date',
            'author': 'Author Full Date',
            'published_date': '2022-06-15',
            'isbn': '1234567890',
            'source': 'GoogleBooks'
        },
        {
            'title': 'Book With Year Only',
            'author': 'Author Year Only',
            'published_date': '2020',
            'isbn': '0987654321',
            'source': 'OpenLibrary'
        },
        {
            'title': 'Book With Invalid Date',
            'author': 'Author Invalid Date',
            'published_date': 'invalid_date',
            'isbn': None,
            'source': 'GoogleBooks'
        },
        {
            'title': 'Book With Unrealistic Year',
            'author': 'Author Unrealistic Year',
            'published_date': '3024',
            'isbn': '1111111111',
            'source': 'OpenLibrary'
        },
        {
            'title': '',  # Missing title
            'author': 'Author Missing Title',
            'published_date': '2021',
            'isbn': '2222222222',
            'source': 'GoogleBooks'
        },
    ]

    # Expected transformed data
    expected_result = [
        {
            'title': 'Book With Full Date',
            'author': 'Author Full Date',
            'published_date': '2022-06-15',
            'isbn': '1234567890',
            'source': 'GoogleBooks'
        },
        {
            'title': 'Book With Year Only',
            'author': 'Author Year Only',
            'published_date': '2020',
            'isbn': '0987654321',
            'source': 'OpenLibrary'
        }
        # The other books are skipped due to missing title, invalid date, or unrealistic year.
    ]

    # Call the function
    result = transform_books_data(raw_data)

    # Assert that the result matches the expected result
    assert result == expected_result
