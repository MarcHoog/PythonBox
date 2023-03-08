from exceptions import CookingItemError
from models import CookingItem
import motor.motor_asyncio

mongodb_connection_string = "mongodb+srv://zamyza:TzMjZU8MQalKsrF8@myatlasclusteredu.4zxg5fi.mongodb.net/?retryWrites=true&w=majority"
mongodb_name = 'python_app'
mongodb_collection = 'first_one'

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_connection_string)
db = client[mongodb_name]


async def bake(name, **kwargs):
    """
    Bakes a CookingItem Into the Database and returns the just created object using find_one from Json.
    """
    await db.first_one.insert_one(dict(CookingItem(name, **kwargs)))
    return await find_one(name)


async def find_one(name):
    """
    Returns a CookingItem object by name, from the MongoDB returns None if Object not found
    :return: CookingItem
    """
    result = await db.first_one.find_one({'name': name})
    if result:
        return CookingItem(**result)
    return None


async def update_one(cooking_item: CookingItem, **kwargs):
    """
    Updates the given cooking with the given kwargs aswel as the related MongoDB document
    Because of this the _ID is not allowed to be changed
    """
    new_values = {}
    if '_id' in kwargs.keys():
        raise CookingItemError('Cannot update _id')

    for key, value in kwargs.items():
        setattr(cooking_item, key, value)
        new_values[key] = value
    await db.first_one.update_one({'_id': cooking_item.id}, {'$set': new_values})
    return cooking_item


async def main():
    # result = await bake(name='walrus', description='another fruit',
    #                    tags=[{'texture': 'cruchy'}])
    ci = await bake(name='mamut', description='another fish', tags=[{'type': 'texture', 'value': 'mushy'}])
    print(dict(ci))


if __name__ == '__main__':
    # item = CookingItem('apple', 'a Fruit', [CookingTag('texture', 'cruchy'), CookingTag('flavor', 'sweet')])
    loop = client.get_io_loop()
    loop.run_until_complete(main())
