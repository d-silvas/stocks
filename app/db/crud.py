from datetime import datetime
from contextlib import contextmanager

from sqlalchemy import create_engine
from .config import DATABASE_URI
# from .models import Base, Book
from .models import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy import and_

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# def test_fun():
#     recreate_database()

#     book = Book(
#         title='Deep Learning',
#         author='Ian Goodfellow',
#         pages=775,
#         published=datetime(2016, 11, 18)
#     )

#     with session_scope() as s:
#         s.add(book)
#         s.commit()
#         # s.query(Book).first()
#         # s.query(Book.all())
#         # r = s.query(Book).filter(Book.title.ilike('deep%')).first()
#         r = s.query(Book).filter(
#             and_(
#                 Book.pages > 750,
#                 Book.published > datetime(2016, 1, 1)
#             )
#         ).order_by(Book.pages.desc()).limit(2).all()
#         print(r)