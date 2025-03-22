# pip install pony

from pony.orm import Database, Required, Set, PrimaryKey, db_session

db = Database()

db.bind(provider="sqlite", filename="library2.db", create_db=True)

class Author(db.Entity):
    _table_ = "authors"
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set("Book") # relaccja O2M

class Genre(db.Entity):
    _table_ = "genres"
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    books = Set("Book", table="book_genre", column="genre_id") # relacja M2M

class Book(db.Entity):
    _table_ = "books"
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    year = Required(int)
    author = Required(Author, column="author_id")
    genres = Set(Genre, table="book_genre", column="book_id")


db.generate_mapping(create_tables=True)


@db_session
def add_data():
    author = Author(name="J.R. Tolkien")

    book1 = Book(title="Lords of the Ring", year=1954, author=author)
    book2 = Book(title="Silmarillion", year=1977, author=author)

    fantasy = Genre(name="fantasy")

    book1.genres.add(fantasy)
    book2.genres.add(fantasy)

add_data()
