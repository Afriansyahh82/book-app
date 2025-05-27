from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)

# Configure CORS - more permissive for development
CORS(app, 
     origins=["http://localhost:8080", "http://localhost:5173", "http://127.0.0.1:8080", "http://127.0.0.1:5173"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
     supports_credentials=True)

# Add a test endpoint to check CORS
@app.route('/api/test', methods=['GET', 'OPTIONS'])
def test_cors():
    return jsonify({"message": "CORS is working!"})

# Load books from JSON file
def load_books():
    try:
        with open('books.json', 'r') as f:
            data = json.load(f)
            return data.get('books', [])
    except FileNotFoundError:
        return []

def load_lib():
    try:
        with open('library.json', 'r') as f:
            data = json.load(f)
            return data.get('library', [])
    except FileNotFoundError:
        return []

# Save books to JSON file
def save_books(books_data):
    with open('books.json', 'w') as f:
        json.dump({'books': books_data}, f, indent=2)
def save_lib(libs_data):
    with open('library.json', 'w') as f:
        json.dump({'library': libs_data}, f, indent=2)
# Initialize books from JSON file
books = load_books()
library = load_lib()

@app.route('/api/books', methods=['GET', 'OPTIONS'])
def get_books():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    return jsonify(books)

@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json
    book = {
        'id': len(books) + 1,
        'title': data.get('title'),
        'author': data.get('author'),
        'cover': data.get('cover', ''),  # Book cover image URL
        'rating': data.get('rating', 0),  # Book rating (0-5)
        'pages': data.get('pages', 0),    # Number of pages
        'genre': data.get('genre', ''),   # Book genre
        'status': data.get('status', 'want-to-read')  # Reading status
    }
    books.append(book)
    save_books(books)  # Save to JSON file
    return jsonify(book), 201

@app.route('/api/books/<int:book_id>', methods=['PUT', 'OPTIONS'])
def add_library(book_id):
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    book_found = False
    for book in books:
        if book['id'] == book_id:
            book['status'] = 'read'
            book_found = True
            break

    if not book_found:
        return jsonify({'error': 'Book not found'}), 404

    new_lib = {
        'book_id': book_id
    }
    library.append(new_lib)

    save_books(books)       # Simpan seluruh list books
    save_lib(library)       # Simpan library
    return jsonify({'message': 'Book added to library', 'book_id': book_id}), 200


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for i, book in enumerate(books):
        if book['id'] == book_id:
            deleted_book = books.pop(i)
            save_books(books)  # Save to JSON file
            return jsonify(deleted_book)
    return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5001")
    print("CORS enabled for development")
    app.run(debug=True, port=5001, host='0.0.0.0') 