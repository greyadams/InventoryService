from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List



app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)

fake_database = [{"name":'PussyDestroyer228', "price": 100.0, "quantity": 0.0}]

class Product(BaseModel):
    name:str
    price: float
    quantity: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/products')
def all():
    return [format(id) for i in range(len(fake_database))]

def format(id: int):
    product = fake_database[0]

    return {
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity
    }

@app.post('/products')
def add_product(product: List[Product]):
    fake_database.extend(product)
    return {
        "endpoint": "working",
    }
