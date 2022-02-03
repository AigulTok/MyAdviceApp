import requests

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def hello_page():
    return 'Welcome to My Advice Project!'

@app.get("/about")
def my_about():
    return 'The main purpose of this project is to make you feel better either you are upset or feeling down. ' \
           'A good advice will cheer you up!'


@app.get('/advice')
def my_advice():
    url = 'https://api.adviceslip.com/advice'

    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()

        return result['slip']['advice']
    else:
        return 'Хватит слушать чужие советы, думай своей головой;)'


    #     return {
    #         'advice': result['advice'],
    #         'activeCases': result["advice"],
    #         'newCases': result['New Cases_text']
    #     }
    # else:
    #     return 'Opps! Проблема с источником данных'

# api = 'https://api.adviceslip.com/advice'
# advice = requests.get(api).text
# print(advice)

# https://api.adviceslip.com/advice random advice
# https://api.adviceslip.com/advice/{slip_id} advice by ID
# https://api.adviceslip.com/advice/search/{query} searching advice