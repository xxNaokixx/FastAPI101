from fastapi import FastAPI
from typing import Optional, List
from pydantic import BaseModel

class ShopInfo(BaseModel):
    name:str
    location:str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float]=None

class Data(BaseModel):
    shop_info:Optional[ShopInfo] = None
    items: List[Item]

app = FastAPI()

@app.post("/")
async def index(data: Data):
    return {"data":data}

@app.get("/countries/")
async def country(country_name: Optional[str]=None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no
        }



