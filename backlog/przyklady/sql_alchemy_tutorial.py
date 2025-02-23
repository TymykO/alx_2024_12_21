from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# Konfiguracja bazy danych
db_url = "sqlite:///library.db"
engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definiowanie relacji Many-to-Many między Book i Genre
book_genre_table = Table('book_genre', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)

# Definicja modeli

class Author(Base):
    """Model autora książek"""
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", back_populates="author")

class Genre(Base):
    """Model gatunku książki"""
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre_table, back_populates="genres")

class Book(Base):
    """Model książki"""
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre_table, back_populates="books")

# Tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

# Funkcje operujące na bazie danych
def add_data():
    try:
        author1 = Author(name="George Orwell")
        author2 = Author(name="J.K. Rowling")
        
        book1 = Book(title="1984", year=1949, author=author1)
        book2 = Book(title="Animal Farm", year=1945, author=author1)
        book3 = Book(title="Harry Potter and the Philosopher's Stone", year=1997, author=author2)
        book4 = Book(title="Harry Potter and the Chamber of Secrets", year=1998, author=author2)
        
        fiction = Genre(name="Fiction")
        dystopian = Genre(name="Dystopian")
        
        book1.genres.append(fiction)
        book1.genres.append(dystopian)
        book2.genres.append(fiction)
        book3.genres.append(fiction)
        
        session.add_all([author1, author2, book1, book2, book3, book4, fiction, dystopian])
        session.commit()
    except Exception as e:
        print(f"Wystąpił błąd podczas dodawania danych: {e}")
        

def get_all_authors():
    authors = session.query(Author).all()
    for author in authors:
        print(f"Autor: {author.name}")

def get_books_by_author(author_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if author:
        print(f"Książki autora {author.name}:")
        for book in author.books:
            print(f"- {book.title} ({book.year})")

def get_recent_books():
    books = session.query(Book).filter(Book.year > 1950).all()
    for book in books:
        print(f"{book.title} - {book.year}")

def update_book_title(old_title, new_title):
    book = session.query(Book).filter_by(title=old_title).first()
    if book:
        book.title = new_title
        session.commit()
        print(f"Zmieniono tytuł na: {new_title}")

def delete_book(book_title):
    book = session.query(Book).filter_by(title=book_title).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Książka '{book_title}' została usunięta.")

def get_book_genres(book_title):
    book = session.query(Book).filter_by(title=book_title).first()
    if book:
        print(f"Gatunki książki '{book.title}':")
        for genre in book.genres:
            print(f"- {genre.name}")

# Przykładowe uruchomienie skryptu
if __name__ == "__main__":
    # add_data()
    get_all_authors()
    get_books_by_author("George Orwell")
    get_recent_books()
    update_book_title("1984", "Nineteen Eighty-Four")
    delete_book("Animal Farm")
    get_book_genres("Nineteen Eighty-Four")
