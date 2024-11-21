import pytest
from unittest.mock import patch, MagicMock
from dags.load import load_books_data


def test_load_books_data():
    # Mock transformed data
    transformed_data = [
        {
            'title': 'Test Book 1',
            'author': 'Author 1',
            'published_date': 2023,
            'isbn': '1234567890'
        },
        {
            'title': 'Test Book 2',
            'author': 'Author 2',
            'published_date': 2022,
            'isbn': '0987654321'
        }
    ]

    # Mock the database engine and connection
    with patch('dags.load.create_engine') as mock_create_engine:
        mock_engine = MagicMock()
        mock_connection = mock_engine.connect.return_value.__enter__.return_value
        mock_create_engine.return_value = mock_engine

        # Set up mocked responses for `execute` calls
        def mock_execute(query, *args, **kwargs):
            query = query.strip().lower()  # Normalize query formatting
            if "select count(*) from books" in query:
                if not hasattr(mock_execute, "count"):
                    mock_execute.count = 0  # Initialize counter
                if mock_execute.count == 0:
                    mock_execute.count += 1
                    return MagicMock(scalar=lambda: 1)  # `before_count`
                return MagicMock(scalar=lambda: 2)  # `after_count`
            elif "create table" in query:
                return None  # Simulate table creation
            elif "insert into" in query:
                return None  # Simulate insert queries
            elif "select isbn, count(*) from books" in query:
                mock_result = MagicMock()
                mock_result.fetchall.return_value = []  # No duplicates
                return mock_result
            else:
                raise ValueError(f"Unexpected query: {query}")

        mock_connection.execute.side_effect = mock_execute

        # Call the `load_books_data` function
        load_books_data(transformed_data)

        # Inspect the call arguments for `mock_connection.execute`
        queries = [call[0][0].strip().lower() for call in mock_connection.execute.call_args_list]

        # Assertions
        assert any("create table if not exists books" in query for query in queries)
        assert any("create table if not exists metadata" in query for query in queries)
        assert any("select count(*) from books" in query for query in queries)
        assert any("insert into books" in query for query in queries)
        assert any("insert into metadata" in query for query in queries)
