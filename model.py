

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class fiche(Base):

    __tablename__='fiches'

    id = Column(Integer,primary_key=True)
    title = Column(String(40))
    text_content = Column(String(40))
    created = 