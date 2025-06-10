from typing import List # for type hinting
from fastapi import FastAPI # for creating the API
from pydantic import BaseModel # for data validation eg.) to validate the request body

app = FastAPI()  # Create an instance of FastAPI

class Tea(BaseModel):
    id: int 
    name: str
    origin: str

teas: List[Tea] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API!"}

@app.get("/teas")
def get_teas():
    return teads

@app.post("/teas")
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.get("/teas/{tea_id}")
def get_tea(tea_id: int):
    for tea in teas:
        if tea.id == tea_id:
            return tea
    return {"error": "Tea not found"}, 404

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    return {"error": "Tea not found"}, 404

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            del teas[index]
            return {"message": "Tea deleted successfully"}
    return {"error": "Tea not found"}, 404

