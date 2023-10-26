from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Gender, Role , UserUpdateRequest
from uuid import uuid4, UUID

app = FastAPI()

db : List[User] = [
    User(
        id = UUID("bd679b15-a2f0-4a06-b342-bf76cc3dabdc"),
        first_name = "Drashti",
        last_name = "Kumbhani",
        middle_name = "Himmatbhai",
        gender = Gender.female,
        roles = [Role.student]
    ),
    User(
        id = UUID("014ecc14-124e-4bda-9c08-f4054c2ed3cc"),
        first_name = "Jinal",
        last_name = "Khanadhar",
        middle_name = "Rajeshbhai",
        gender = Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    # await foo()
    return {"Hello" : "Drashti"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id : UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404, 
        detail=f"user with id : {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return 
    raise HTTPException(
        status_code=404,
        details=f"user with id: {user.id} does not exists"
    )
