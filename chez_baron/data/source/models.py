from pydantic import BaseModel


class Tag(BaseModel):
    type: str
    value: str


class Ingredient(BaseModel):
    name: str
    description: str
    thumbnail: str
    tags: list[Tag] | None = None
    recommendations: list[str] | None = None


class Recipy(BaseModel):
    name: str
    description: str
    ingredients: list[Ingredient] | None = None
    steps: list[str] | None = None