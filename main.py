from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

# Fake DB (in memory list)
users = []

@app.get("/")
def home():
    return {"message": "API with CRUD is running!"}

@app.post("/user")
def create_user(user: User):
    users.append(user)
    return {"status": "user added", "data": user}

@app.get("/users")
def get_users():
    return {"total": len(users), "users": users}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User):
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = updated_user
    return {"status": "user updated", "data": updated_user}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    if user_id >= len(users) or user_id < 0:
        raise HTTPException(status_code=404, detail="User not found")
    deleted_user = users.pop(user_id)
    return {"status": "user deleted", "data": deleted_user}
