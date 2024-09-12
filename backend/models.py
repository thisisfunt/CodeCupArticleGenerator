from pydantic import BaseModel
import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select

class Author(BaseModel):
    name: str
    description: str
    keywords: str
    specialization: str
    tone: str


def create_author(author: Author):
    with Session(schemas.engine) as session:
        author = schemas.Author(
            name=author.name,
            description=author.description,
            keywords=author.keywords,
            specialization=author.specialization,
            tone=author.tone
        )
        session.add(author)
        session.commit()
        return author.id


def get_author(id: int):
    with Session(schemas.engine) as session:
        stmt = select(schemas.Author).where(schemas.Author.id==id)
        author = session.scalars(stmt).one()
        return author

def delete_author(id: int):
    with Session(schemas.engine) as session:
        author = session.get(schemas.Author, id)
        session.delete(author)
        session.commit()

def update_author(author_id: int, authorData: Author):
    with Session(schemas.engine) as session:
        author = session.query(schemas.Author).get(author_id)
        author.name = authorData.name
        author.description = authorData.description
        author.keywords = authorData.keywords
        author.specialization = authorData.specialization
        author.tone = authorData.tone
        session.commit()
        