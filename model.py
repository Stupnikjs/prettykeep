

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class fiche(Base):

    __tablename__='fiches'

    id = Column(Integer,primary_key=True)
    title = Column(String(40))
    text_content = Column(String(40))
    created = Column(String(20))
    updated = Column(String(20))

   def to_dict():
     return {
     'title':self.title, 
     'text_content' : self.text_content,
     'created' : self.created,
      'updated': self.updated
      
}

    def __str__(self):
        return self.to_dict()