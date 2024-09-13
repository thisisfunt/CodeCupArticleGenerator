from pydantic import BaseModel
import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select
from dotenv import dotenv_values
from openai import OpenAI


ENV_VARIABLES = dotenv_values(".env")

openAI = OpenAI(
    api_key=ENV_VARIABLES["OPENAI_KEY"],
    base_url=ENV_VARIABLES["OPENAI_BASE_URL"]
)



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

def get_trends():
    completion = openAI.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': 'Составь список 20 актуальных трендов в мировом сообществе в формате "тренд 1|тренд 2|тренд 3..." без дополнительных комментариев.',
            }
        ],
        model='gpt-3.5-turbo',
    )
    answer = completion.choices[0].message.content
    trends = answer.split("|")
    return trends

def get_themes(trend: str):
    completion = openAI.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'Составь список тем для статей на тему "{trend}"  в формате "тема 1|тема 2|тема 3..." без дополнительных комментариев.',
            }
        ],
        model='gpt-3.5-turbo',
    )
    answer = completion.choices[0].message.content
    themes = answer.split("|")
    return themes


def create_article(author_id: int, theme: str, min_len: int):
    author = get_author(author_id)
    completion = openAI.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f'Напиши статью от на тему "{theme}" от лица человека, который "{author.description}" и хорошо разбирается в "{author.specialization}", речь которого "{author.keywords}", тон которого должен быть "{author.tone}". Постарайся отразить в тексте особенности автора, но не проговаривать их напрямую без необходимости. Длинна текста должна привышать {min_len} токенов',
            }
        ],
        model='gpt-3.5-turbo',
    )
    article = completion.choices[0].message.content
    return article