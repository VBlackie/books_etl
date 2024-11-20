from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def validate_loaded_data(connection):
    # Check for duplicates in the `books` table
    duplicates_query = """
    SELECT isbn, COUNT(*) FROM books
    GROUP BY isbn
    HAVING COUNT(*) > 1;
    """
    duplicates = connection.execute(duplicates_query).fetchall()
    if duplicates:
        logging.error(f"Duplicate records found in database: {duplicates}")
        raise ValueError("Duplicate records detected in the `books` table.")
    logging.info("Database validated successfully.")


def load_books_data(transformed_data, **kwargs):
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres-books-db:5432/books_db')

    try:
        logging.info("Starting the data loading process...")

        with engine.connect() as connection:
            # Ensure tables exist
            logging.info("Ensuring the 'books' and 'metadata' tables exist.")
            connection.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    published_date INT,
                    isbn VARCHAR(20) UNIQUE
                );
            """)
            connection.execute("""
                CREATE TABLE IF NOT EXISTS metadata (
                    id SERIAL PRIMARY KEY,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    total_records INT,
                    new_records INT,
                    existing_records INT
                );
            """)

            # Log before counting existing records
            logging.debug("Counting existing records in 'books' table...")
            before_count = connection.execute("SELECT COUNT(*) FROM books").scalar()

            # Insert data
            logging.info("Inserting new books into the 'books' table.")
            for book in transformed_data:
                title = book['title'].replace("'", "''")
                author = book['author'].replace("'", "''")
                published_date = book['published_date']
                isbn = book['isbn']

                try:
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
                    logging.debug(f"Inserted book: {title} by {author}.")
                except Exception as insert_error:
                    logging.warning(f"Failed to insert book '{title}' by '{author}': {insert_error}")

            # Log after counting total records
            logging.debug("Counting total records in 'books' table after insertion...")
            after_count = connection.execute("SELECT COUNT(*) FROM books").scalar()

            # Calculate new and existing records
            new_records = after_count - before_count
            existing_records = before_count  # Since duplicates were skipped

            # Validation for loaded data
            validate_loaded_data(connection)
            logging.info(f"Books added: {new_records}, Total books: {after_count}, Existing books: {existing_records}")

            # Insert metadata
            logging.info("Updating metadata table with record counts.")
            connection.execute(f"""
                INSERT INTO metadata (total_records, new_records, existing_records)
                VALUES ({after_count}, {new_records}, {existing_records});
            """)

        logging.info("Data loading process completed successfully.")

    except Exception as e:
        logging.critical(f"An error occurred during the data loading process: {e}")
        raise
