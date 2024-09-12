from fastapi import FastAPI
import models


app = FastAPI()


#done
@app.get("/author/{author_id}")
async def get_author(author_id: int):
    author = models.get_author(author_id)
    return {
        "id": author_id,
        "name": author.name,
        "description": author.description,
        "keywords": author.keywords,
        "specialization": author.specialization,
        "tone": author.tone
    }

#done
@app.put("/author/{author_id}")
async def update_author(author_id: int, author: models.Author):
    models.update_author(author_id, author)
    return {
        "status": "OK",
        "id": 31
    }

#done
@app.post("/author")
async def create_author(author: models.Author):
    id = models.create_author(author)
    return {
        "status": "OK",
        "id": id
    }

#done
@app.delete("/author/{author_id}")
async def delete_author(author_id: int):
    models.delete_author(author_id)
    return {
        "status": "OK"
    }


@app.get("/trends")
async def get_trends():
    return ["Economic", "Politic", "Sport"]


@app.get("/themes/{trend}")
async def get_themes(trend):
    return ["Top the most popular sport in 2024", "How to start play basketball"]


@app.get("/article")
async def create_article(authorId: int, theme: str, min_len: int):
    return {
        "text": "askfhsdlfshfslsjsfksf;jfpqw idofujewpfd pwufwpofuwp owfowdfjwpo wdufpwdfowufpwfuw pfwdfw-fwfwofiw wdif-wdifwd-f0wifw",
        "pipelines": ["google.com", "yandex.ru"]
    }