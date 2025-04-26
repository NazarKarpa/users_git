from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [
    {
        'login': "admin",
        'name': 'Volodymyr',
        'surname': 'Hubash',
        'age': 25,
    }
]


class User(BaseModel):
    login: str
    name: str
    surname: str
    age: int


@app.get("/")
async def get_all_users():

    return {'messgae': 'hello, world'}


@app.get("/users/all")
async def get_all_users():
    """
    Повертає дані про всіх користувачів
    """
    return users


@app.post("/users/new/")
async def add_new_user(new_user: User):
    """
    Додає нового користувача з login, name, surname, age
    """
    users.append({
        "login": new_user.login,
        "name": new_user.name,
        "surname": new_user.surname,
        "age": new_user.age,
    })

    return {'message': "Користувача додано"}
