import requests

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def get_advice_from_api():
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url)
    if r.status_code == 200:
        result = r.json()
        return result["slip"]["advice"]
    else:
        return 'Хватит слушать чужие советы, думай своей головой;)'


@app.get("/", response_class=HTMLResponse)
def get_advice(request: Request):

    responses = []
    for i in range(3):
        responses.append(get_advice_from_api())

    data = {
        "request": request,
        "result1": responses[0],
        "result2": responses[1],
        "result3": responses[2],
    }
    return templates.TemplateResponse("index.html", data)

















@app.get("/home", response_class=HTMLResponse)
def hello_page(request: Request):
    hello_data = {
            "request": request}
    return templates.TemplateResponse("item.html", hello_data)


@app.get("/about", response_class=HTMLResponse)
def my_about(request: Request):
    about_data = {
        "request": request}
    return templates.TemplateResponse("about.html", about_data)


@app.get("/project", response_class=HTMLResponse)
def my_project(request: Request):
    responses = []
    for i in range(3):
        responses.append(get_advice_from_api())

    data = {
        "request": request,
        "result1": responses[0],
        "result2": responses[1],
        "result3": responses[2],
    }
    return templates.TemplateResponse("project.html", data)


@app.get("/author", response_class=HTMLResponse)
def my_about(request: Request):
    author_data = {
        "request": request}
    return templates.TemplateResponse("author.html", author_data)





