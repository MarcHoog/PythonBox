from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data import find_one, bake, update_one

app = FastAPI()


class CookingItemBM(BaseModel):
    name: str
    description: str | None = None
    tags: list[dict] | None = None
    recommendations: list[str] | None = None


@app.get('/api/{item_name}', status_code=200)
async def root(item_name: str):
    result = await find_one(item_name)
    if result is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return result


@app.post('/api/bake', status_code=201)
async def bake_item(item: CookingItemBM):
    if await find_one(item.name) is not None:
        raise HTTPException(status_code=409, detail="Item already exists")
    result = await bake(item.name, description=item.description, tags=item.tags)
    return result


@app.post('/api/')
async def post():
    pass


if __name__ == '__main__':
    print('Hello World')
