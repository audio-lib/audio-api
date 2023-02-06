from fastapi import FastAPI
from urllib.parse import unquote
from fastapi.openapi.utils import get_openapi

import model

app = FastAPI()


# api/authors
# Возвращает ответ в виде [{"author": "..."}, {"author": "..."}]
@app.get("/api/authors")
async def get_all_authors():
    return list(model.Records.select())


# api/authors/:authorName/audiobooks
# [{"author": "...", "title": "...", "link": "..."}]
@app.get("/api/{author_name}/audiobooks")
async def get_books_from_author(author_name: str):
    s = unquote(author_name, 'cp1251')
    return list(model.Records.select().where(model.Records.author.contains(s)))


# api/audiobooks?title=...

@app.get("/api/audiobooks")
async def get_books_from_author(title: str):
    s = unquote(title, 'cp1251')
    return list(model.Records.select().where(model.Records.title.contains(s)))


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title='audio_api', version="2.5.0", description='Документация API для проекта',
                         routes=app.routes)
    app.openapi_schema = schema


app.openapi = custom_openapi
