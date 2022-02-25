import fastapi
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.applications import get_swagger_ui_html
from bs4 import BeautifulSoup


def patched_openapi_docs(*args, **kwargs):
    docs_html = get_swagger_ui_html(*args, **kwargs)
    docs = BeautifulSoup(docs_html.body, "html.parser")
    dark_mode_css = BeautifulSoup('<link rel="stylesheet" href="/static/dark_mode.css" type="text/css">')
    docs.head.insert(0, dark_mode_css)
    return HTMLResponse(str(docs))


fastapi.applications.get_swagger_ui_html = patched_openapi_docs

app = FastAPI(
    title="Test",
    description="""
    **Scaryyyy**
    """,
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hell:o World"}


@app.get("/oshrita")
async def root1():
    return {"message": "Hell:o World"}


@app.get("/nir")
async def root2():
    return {"message": "Hell:o World"}
