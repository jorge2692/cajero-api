from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    password: str
    balance: int

database_users = {
    "Jorge": UserInDB(**{"username": "Jorge", "password": "root", "balance": 120000}),
    "Mario": UserInDB(**{"username": "Mario", "password": "hola", "balance": 340000})
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username]= user_in_db
    return user_in_db