import requests

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def hello_page(request: Request):
    hello_data = {
            "request": request}
    return templates.TemplateResponse("item.html", hello_data)


# @app.get("/", response_class=HTMLResponse)
# def hello_page(request: Request):
#     hello_data = {
#             "request": request}
#     return templates.TemplateResponse("index.html", hello_data)


@app.get("/about/", response_class=HTMLResponse)
def my_about(request: Request):
    about_data = {
        "request": request}
    return templates.TemplateResponse("about.html", about_data)


# @app.get("/about/", response_class=HTMLResponse)
# def my_about(request: Request):
#     about_data = {
#         "request": request}
#     return templates.TemplateResponse("index.html", about_data)


@app.get("/project", response_class=HTMLResponse)
def my_advice(request: Request):
    url = 'https://api.adviceslip.com/advice'

    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        data = {
            "request": request,
            "result": result['slip']['advice']
        }

        return templates.TemplateResponse("project.html", data)
    else:
        return 'Хватит слушать чужие советы, думай своей головой;)'


# @app.get("/project", response_class=HTMLResponse)
# def my_advice(request: Request):
#     url = 'https://api.adviceslip.com/advice'
#
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         result = response.json()
#         data = {
#             "request": request,
#             "result": result['slip']['advice']
#         }
#
#         return templates.TemplateResponse("index.html", data)
#     else:
#         return 'Хватит слушать чужие советы, думай своей головой;)'


@app.get("/author/", response_class=HTMLResponse)
def my_about(request: Request):
    author_data = {
        "request": request}
    return templates.TemplateResponse("author.html", author_data)

