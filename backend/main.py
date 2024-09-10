from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def hello():
    return {"answer": "Hello, world!"}


