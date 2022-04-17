from pydantic import BaseModel, HttpUrl, ValidationError, validator, parse

class BaseMessage(BaseModel):
    status: str

'''Плоский список пород или субпород'''
class Breeds(BaseMessage):
    message: list[str]

'''Список пород и субпород'''
class BreedsSubbreeds(BaseMessage):
    message: dict[str, list[str]]

'''Ссылка на отдельное изображение'''
class ImageUrl(BaseMessage):
    message: HttpUrl

'''Список ссылок на изображения'''
class ImageUrlList(BaseMessage):
    message: list[HttpUrl]



data = {"message": {"ass": ['a'], 'bass': []}, "status": "success"}

data = {"message": ['a', 'b'], 'status': 'success'}

data = {"message":"https://images.dog.ceo/breeds/bulldog-boston/n02096585_414.jpg","status":"success"}

data = {"message":["https://images.dog.ceo/breeds/springer-english/n02102040_841.jpg"],"status":"success"}


parsed = ImageUrlList.parse_obj(data)

print(parsed.json())

