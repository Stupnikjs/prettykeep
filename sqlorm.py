
from sqlalchemy import Boolean, ForeignKey, String, Column, Integer, Table
from sqlalchemy.orm import DeclarativeBase, relationship

# tout passer en SQL 

class Base(DeclarativeBase):
    pass


class Fiche(Base):

    __tablename__='fiches'

    id = Column(Integer,primary_key=True)
    title = Column(String(200))
    text = Column(String(2000))
    created = Column(String(20))
    updated = Column(String(20))
    complete_start = Column(Integer)
    complete_end = Column(Integer)
    labels = relationship('Label', secondary='association', back_populates='fiches', lazy='joined')

    def to_dict(self):
        return {
        'id':self.id,
        'title':self.title, 
        'text' : self.text,
        'created' : self.created,
        'labels': self.labels,
        'updated': self.updated,
        'complete_start': self.complete_start,
        'complete_end': self.complete_end
        }

    def __str__(self):
        return self.to_dict()




class Label(Base):

    __tablename__='labels'
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    hot = Column(Boolean)
    fiches = relationship('Fiche', secondary='association', back_populates='labels')

    def to_dict(self):
        return {
        'id':self.id,
        'name': self.name,
        'hot': self.hot 
        }

    def __str__(self):
        return self.to_dict()
    

association_table = Table(
    'association', 
    Base.metadata,
    Column('fiches_id', Integer, ForeignKey('fiches.id')),
    Column('labels_id', Integer, ForeignKey('labels.id'))

)