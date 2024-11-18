import logging

def transform_books_data(raw_data):
    transformed_data = []
    unique_books = set()  # Set to store unique identifiers (ISBN or title-author pairs)

    for book in raw_data:
        # Skip entries with missing title or author
        if not book['title'] or not book['author']:
            continue

        # Use ISBN if available, otherwise use a combination of title and author as the unique identifier
        unique_id = book['isbn'] if book['isbn'] else (book['title'], book['author'])

        # Check if the unique_id is already in the set
        if unique_id in unique_books:
            continue  # Skip this book as it's a duplicate

        # Add the unique_id to the set
        unique_books.add(unique_id)

        # Add the book to the transformed_data list
        transformed_data.append({
            'title': book['title'],
            'author': book['author'],
            'published_date': book['published_date'],
            'isbn': book['isbn']
        })
    logging.info(f"Transformed {len(transformed_data)} unique books.")

    return transformed_data
