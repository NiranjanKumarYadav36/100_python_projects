from flask import Flask, jsonify
import json
app = Flask(__name__)

with open("books.json") as file:
    data = json.load(file)


@app.route('/')
def index():
    return "Homepage"


@app.route('/books/<int:book_id>')
def get_book(book_id):
    books = data.get(book_id) # used get method to avoid key error
    if books:
        return jsonify(books)
    else:
        return "{message: 'Book not found'}", 404


if __name__ == "__main__":
    app.run(debug=True)

