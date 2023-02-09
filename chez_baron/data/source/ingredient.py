from client import client
from models import Ingredient

database = client.cooking_project
collection = database.ingredients


async def fetch_one_ingredient(name):
    document = await collection.find_one({"name": name})
    return document


async def fetch_all_ingredients():
    ingredients = []
    cursor = collection.find()
    async for document in cursor:
        ingredients.append(Ingredient(**document))
    return ingredients


async def create_ingredient(ingredient: dict):
    document = ingredient
    result = await collection.insert_one(document)
    return document


async def update_ingredient_description(name, description):
    await collection.update_one({"name": name}, {"$set": {"description": description}})
    document = await collection.find_one({"name": name})
    return document


async def remove_ingredient(name):
    await collection.delete_one({"name": name})
    return True
