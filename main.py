"""
First, ensure you have fastapi and motor installed in your environment (motor is an async MongoDB driver for Python).
[1] pip install fastapi[all] motor


[2] for run fastapi- python main.py
""" 


from fastapi import FastAPI, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import uvicorn
from pydantic import BaseModel  # Add this import

app = FastAPI()

# MongoDB connection settings
MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "todo_db"

# Dependency to get the database connection
async def get_database():
    client = AsyncIOMotorClient(MONGODB_URL)
    database = client[DATABASE_NAME]
    return database

# Model for Todo
class TodoModel(BaseModel):
    title: str
    description: str

# Routes for CRUD operations
@app.post("/todos/", response_model=TodoModel)
async def create_todo(todo: TodoModel, db: AsyncIOMotorClient = Depends(get_database)):
    collection = db["todos"]
    todo_dict = todo.dict()
    result = await collection.insert_one(todo_dict)
    todo_dict["_id"] = result.inserted_id
    return todo_dict

@app.get("/todos/{todo_id}", response_model=TodoModel)
async def read_todo(todo_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    collection = db["todos"]
    todo = await collection.find_one({"_id": ObjectId(todo_id)})
    if todo:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}", response_model=TodoModel)
async def update_todo(todo_id: str, todo: TodoModel, db: AsyncIOMotorClient = Depends(get_database)):
    collection = db["todos"]
    updated_todo = await collection.update_one({"_id": ObjectId(todo_id)}, {"$set": todo.dict()})
    if updated_todo.modified_count:
        return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    collection = db["todos"]
    deleted_todo = await collection.delete_one({"_id": ObjectId(todo_id)})
    if deleted_todo.deleted_count:
        return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


