from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref, DeclarativeBase
from models.product import Products


class Base(DeclarativeBase):
    pass


class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    review_text = Column(String)
    user_id = Column(Integer)
    date = Column(DateTime)
    product_id = Column(Integer, ForeignKey('products.id'))
    products = relationship(
        Products,
        backref=backref('review',
                        uselist=True,
                        cascade='delete, all'))
    