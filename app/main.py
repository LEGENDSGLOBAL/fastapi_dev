from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()
db = []

@app.get("/")
def index():
	return {"message": "Hello everyone thanks for the opportunity"}


# request pydantic model
class Item(BaseModel):
	id : int
	name : str
	weight : float
	decription : str


# dummy data
items = [{
    "id":  1,
    "name": "name of user",
    "weight": 6.7,
    "description": "creating items for users"
    },

    {
    "id":  2,
    "name": "name of user 2",
    "weight": 6.7,
    "description": "creating items for users"
    }
]

# endpoint to get all data
@app.get("/items")
def get_items():
	return {"data":f"{items}"}

@app.get('/items/{item_id}')
def get_item(item_id: int):
    item = db[item_id-1]
    return {"data":f"{items}"}

@app.get('/items')
def get_items():
    results = []
    for item in db:
    	results.append({'name' : name_of_user['name'], 'weight': items['weight'], 'description': current_time})
    return {"data":f"{items}"}

@app.post('/items')
def create_item(item:Item):
    db.append(item.dict())
    return db[-1]

@app.put('/items/{item_id}')
def update_item(item_id:int,item:Item):
	for key,value in item.dict().items():
            #print(f"{key} : {value}")
            items[item_id-1][key] = value
	return{"data":f"{items[item_id-1]}","message":f"Successfully updated post wihth id {item_id}"}





