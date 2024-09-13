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
    trends = models.get_trends()
    return trends


@app.get("/themes/{trend}")
async def get_themes(trend):
    themes = models.get_themes(trend)
    return themes


@app.get("/article")
async def create_article(author_id: int, theme: str, min_len: int):
    article = models.create_article(author_id, theme, min_len)
    return {
        "text": article,
        "pipelines": ["google.com", "yandex.ru"]
    }