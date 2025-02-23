from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///library.db"
engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

book_genre_table = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genres.id"), primary_key=True),

)

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("Book", back_populates="author")

    def __str__(self):
        return self.name

class Genre(Base):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    books = relationship("Book", secondary=book_genre_table, back_populates="genres")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary=book_genre_table, back_populates="books")


    def __str__(self):
        return f"{self.title} ({self.year})"


Base.metadata.create_all(engine)


def fill_db_with_data():

    author1 = Author(name="George Orwell")
    author2 = Author(name="J. K. Rowling")

    book1 = Book(title="1984", year=1949, author=author1)
    book2 = Book(title="Animal Farm", year=1945, author=author1)
    book3 = Book(title="Harry Potter and the Philosopher's Stone", year=1997, author=author2)
    book4 = Book(title="Harry Potter and the Chamber of Secrets", year=1998, author=author2)

    fiction = Genre(name="Fiction")
    dystopion = Genre(name="Dystopian")

    book1.genres.append(fiction)
    book2.genres.append(dystopion)
    book3.genres.append(fiction)
    book4.genres.append(fiction)

    session.add_all(
        [
        author1, author2, book1, book2,
        book3, book4,
        fiction, dystopion
        ]
    )
    session.commit()


# fill_db_with_data()

def get_all_authors():
    authors = session.query(Author).all()
    for a in authors:
        print(f"Author: {a.name}")

def get_books_by_author_name(author_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if author:
        print(f"Książki autora {author}:")
        for book in author.books:
            print(f" - {book}")

def get_recent_book(year):
    books = session.query(Book).filter(Book.year > year).all()
    for book in books: print(f"- {book}")



def update_book(old_title, new_title):
    book = session.query(Book).filter_by(title=old_title).first()
    if book:
        book.title = new_title
        session.commit()

get_all_authors()
get_books_by_author_name("George Orwell")
get_recent_book(1980)
update_book("1984", "Rok 1984")