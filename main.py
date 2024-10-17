from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
app.title = "App de peliculas"
app.version = "0.0.1"
movies_list =[
    {
        "id": "1",
        "title":"Edgame",
        "año":"2022",
        "desc":"VENGADORES - SUPER HEROES",
    },
    {
        "id": "2",
        "title":"ALIENS",
        "año":"2001",
        "desc":"Invacion alienigena",
    }
]

@app.get('/',tags=["home"])
def message_():
    return HTMLResponse("<h1>Hola world></h1>")

@app.get('/movies',tags=["movies"])
def movies():
    return movies_list

@app.get('/movies/{id}',tags=["movies"])
def movie(id:int):
    for item in movies_list:
        print(item["id"])
        if item["id"] == id:
            return item
        else:
            print("no se enontro tu pelicula por ese id")
    return[]