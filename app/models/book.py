# _*_ coding: utf-8 _*_
from sqlalchemy import Column, Integer, String, Text

from app.models.base import db

__auther__ = "tanran"
__date__ = "2019/1/29 21:53"


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    auther = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(Text)
    image = Column(String(50))

    def sample(self):
        pass