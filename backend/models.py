from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name: str
    description: str
    keywords: str
    specialization: str
    tone: str
