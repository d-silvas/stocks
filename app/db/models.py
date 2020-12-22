from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.postgresql import MONEY

Base = declarative_base()

# class Book(Base):
#     __tablename__='books'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     author = Column(String)
#     pages = Column(Integer)
#     published = Column(Date)
#     price = Column(MONEY)

#     def __repr__(self):
#         return f'<Book(title={self.title}, author={self.author}, pages={self.pages}, published={self.published})'


# TODO created_at, updated_at

class Ticker(Base):
    __tablename__ = 'ticker'
    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True)

class SummaryProfile(Base):
    __tablename__ = 'summary_profile'
    id = Column(Integer, primary_key=True)
    ticker_id = Column(Integer, ForeignKey('ticker.id'))

class SummaryDetail(Base):
    __tablename__ = 'summary_detail'
    id = Column(Integer, primary_key=True)
    ticker_id = Column(Integer, ForeignKey('ticker.id'))

class IncomeStatement(Base):
    __tablename__ = 'income_statement'
    id = Column(Integer, primary_key=True)
    ticker_id = Column(Integer, ForeignKey('ticker.id'))
    as_of_date = Column(Date)
    period_type = Column(String)
    basic_average_shares = Column(MONEY)
    basic_eps = Column(MONEY)
    cost_of_revenue = Column(MONEY)
    ebit = Column(MONEY)
    ebitda = Column(MONEY)
