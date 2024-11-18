from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_books_data(transformed_data, **kwargs):
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres-books-db:5432/books_db')
    try:
        with engine.connect() as connection:
            logging.info("Ensuring tables exist...")
            # Create books table if it doesn't exist
            connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    published_date INT,
                    isbn VARCHAR(20) UNIQUE
                );
            """)

            # Create metadata table if it doesn't exist
            connection.execute("""
                CREATE TABLE IF NOT EXISTS metadata (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_records INT,
                    new_records INT,
                    existing_records INT
                );
            """)

            # Count total records before insertion
            before_count = connection.execute("SELECT COUNT(*) FROM books").scalar()

            # Insert data
            for book in transformed_data:
                title = book['title'].replace("'", "''")
                author = book['author'].replace("'", "''")
                published_date = book['published_date']
                isbn = book['isbn']

                insert_query = f"""
                INSERT INTO books (title, author, published_date, isbn)
                VALUES (
                    '{title}',
                    '{author}',
                    {published_date if published_date else 'NULL'},
                    '{isbn if isbn else ''}'
                )
                ON CONFLICT (isbn) DO NOTHING;
                """
                connection.execute(insert_query)

            # Count total records after insertion
            after_count = connection.execute("SELECT COUNT(*) FROM books").scalar()

            # Calculate new and existing records
            new_records = after_count - before_count
            existing_records = before_count  # Since we skipped duplicates
            logging.info(f"Books added: {new_records}, Total books: {after_count}")

            # Insert metadata
            connection.execute(f"""
                INSERT INTO metadata (total_records, new_records, existing_records)
                VALUES ({after_count}, {new_records}, {existing_records});
            """)

    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
        raise
