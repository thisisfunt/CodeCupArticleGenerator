from fastapi import FastAPI
import models


app = FastAPI()


@app.get("/author/{id}")
async def get_author(id: int):
    return {
        "id": id,
        "name": "Alex",
        "description": "Young guy with broken heart",
        "keywords": "Simple worlds and teen slang",
        "specialization": "programming and music",
        "tone": "not official"
    }

@app.post("/author")
async def create_author(author: models.Author):
    return {
        "status": "OK",
        "id": 31
    }

@app.put("/author")
async def put_author(author: models.Author):
    return {
        "status": "OK",
        "id": 31
    }

@app.delete("/author")
async def delete_author(author: models.Author):
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