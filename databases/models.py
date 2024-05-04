from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column



class Base(DeclarativeBase):
    pass



# this represents the books table in SQLAlchemy version 2(Declarative approach)

class Book(Base):
    __tablename__="books"
    id:Mapped[int]=mapped_column(primary_key=True)
    title:Mapped[str]=mapped_column()
    author:Mapped[str]=mapped_column()
    year:Mapped[int]=mapped_column()
    isbn:Mapped[str]=mapped_column()
    
    
