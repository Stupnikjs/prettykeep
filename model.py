
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Fiche(Base):

    __tablename__='fiches'

    id = Column(Integer,primary_key=True)
    title = Column(String(200))
    text = Column(String(2000))
    created = Column(String(20))
    updated = Column(String(20))
    labels = Column(String(30))
    complete_start = Column(Integer)
    complete_end = Column(Integer)

    def to_dict(self):
        return {
        'title':self.title, 
        'text' : self.text,
        'created' : self.created,
        'updated': self.updated,
        'labels': self.labels,
        'complete_start': self.complete_start,
        'complete_end': self.complete_end
        }

    def __str__(self):
        return self.to_dict()