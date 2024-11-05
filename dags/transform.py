def transform_books_data(raw_data):
    transformed_data = []
    for book in raw_data:
        if not book['title'] or not book['author']:
            continue  # Skip entries with missing title or author
        # Additional data cleaning can be done here if needed
        transformed_data.append({
            'title': book['title'],
            'author': book['author'],
            'published_date': book['published_date'],
            'isbn': book['isbn']
        })
    return transformed_data
