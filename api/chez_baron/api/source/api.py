from python.chez_baron.data import (
    fetch_one_ingredient,
    fetch_all_ingredients,
    create_ingredient,
    remove_ingredient
)

from python.chez_baron.data.source.ingredient import (
    fetch_one_ingredient,
)

from fastapi import FastAPI, HTTPException
from chez_baron.data.source import Ingredient

app = FastAPI()


@app.get('/')
async def read_root():
    return {"ping": "pong"}


@app.get("/api/ingredients")
async def get_ingredients():
    response = await fetch_all_ingredients()
    return response


@app.get("/api/ingredients/{name}", response_model=Ingredient)
async def get_ingredient_by_name(name):
    response = await fetch_one_ingredient(name)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f"There is no ingredient with this name {name}")


@app.post("/api/ingredients", response_model=Ingredient)
async def post_ingredient(ingredient: Ingredient):
    if await fetch_one_ingredient(ingredient.name):
        raise HTTPException(status_code=409, detail=f"Ingredient {ingredient.name} already exists")

    response = await create_ingredient(ingredient.dict())
    if response:
        return response
    raise HTTPException(status_code=400,
                        detail=f"Something went wrong / Bad Request")


@app.delete("/api/ingredients/{name}")
async def delete_ingredient(name):
    response = await remove_ingredient(name)
    if response:
        return response
    raise HTTPException(status_code=404,
                        detail=f"There is no ingredient with this name {name}")
