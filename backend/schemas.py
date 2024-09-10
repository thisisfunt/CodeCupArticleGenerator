from sqlalchemy import create_engine, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_engine("sqlite:///database.db", echo=True)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Author(Base):
    __tablename__="authors"
    name: Mapped[str] = mapped_column(String())
    description: Mapped[str] = mapped_column(String())
    keywords: Mapped[str] = mapped_column(String())
    specialization: Mapped[str] = mapped_column(String())
    tone: Mapped[str] = mapped_column(String())

class Article(Base):
    __tablename__="articles"
    theme: Mapped[str] = mapped_column(String())
    text: Mapped[str] = mapped_column(String())
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))


Base.metadata.create_all(engine)