from random import sample

import pytest
from pydantic import BaseModel, HttpUrl, ValidationError
from src.api.simple_api_client import SimpleApiClient


class Geo(BaseModel):
    lat: str
    lng: str


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company


class UserList(BaseModel):
    __root__: list[User]


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PostList(BaseModel):
    __root__: list[Post]


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class CommentList(BaseModel):
    __root__: list[Comment]


class Album(BaseModel):
    userId: int
    id: int
    title: str


class AlbumList(BaseModel):
    __root__: list[Album]


class Photo(BaseModel):
    albumId: int
    id: int
    title: str
    url: HttpUrl
    thumbnailUrl: HttpUrl


class PhotosList(BaseModel):
    __root__: list[Photo]


class Todo(BaseModel):
    userId: int
    id: int
    title: str
    completed: bool


class TodosList(BaseModel):
    __root__: list[Todo]


def validate_object(cls, obj):
    try:
        cls.parse_obj(obj)
    except ValidationError as e:
        print(e.json())
        pytest.fail()


proxies = {
    "http": "http://localhost:8080",
    "https": "http://localhost:8080"
}

base_url = 'https://jsonplaceholder.typicode.com'


def choises(r, n):
    return sample(range(1, r), n)


@pytest.fixture(scope='session')
def api():
    yield SimpleApiClient(url=base_url, verify=False, proxies=None)


def test_get_all_users(api):
    r = api.GET('/users')
    assert r.ok
    validate_object(UserList, r.json())


def test_get_all_posts(api):
    r = api.GET('/posts')
    assert r.ok
    validate_object(PostList, r.json())


def test_get_all_albums(api):
    r = api.GET('/albums')
    assert r.ok
    validate_object(AlbumList, r.json())


def test_get_all_photos(api):
    r = api.GET('/photos')
    assert r.ok
    validate_object(PhotosList, r.json())


def test_get_all_todos(api):
    r = api.GET('/todos')
    assert r.ok
    validate_object(TodosList, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_single_user(api, userid):
    r = api.GET(f'/users/{userid}')
    assert r.ok
    validate_object(User, r.json())


@pytest.mark.parametrize('postid', choises(100, 5))
def test_get_single_post(api, postid):
    r = api.GET(f'/posts/{postid}')
    assert r.ok
    validate_object(Post, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_single_posts_by_user(api, userid):
    r = api.GET(f'/posts', params={'userId': userid})
    assert r.ok
    validate_object(PostList, r.json())


@pytest.mark.parametrize('postid', choises(100, 5))
def test_get_comments(api, postid):
    r = api.GET(f'/posts/{postid}/comments')
    assert r.ok
    validate_object(CommentList, r.json())


@pytest.mark.parametrize('postid', choises(100, 5))
def test_get_comments_by_post(api, postid):
    r = api.GET(f'/comments', params={'postId': postid})
    assert r.ok
    validate_object(CommentList, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_albums(api, userid):
    r = api.GET(f'/users/{userid}/albums')
    assert r.ok
    validate_object(AlbumList, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_albums_by_user(api, userid):
    r = api.GET(f'/albums', params={'userId': userid})
    assert r.ok
    validate_object(AlbumList, r.json())


@pytest.mark.parametrize('albumid', choises(100, 5))
def test_get_photos(api, albumid):
    r = api.GET(f'/albums/{albumid}/photos')
    assert r.ok
    validate_object(PhotosList, r.json())


@pytest.mark.parametrize('albumid', choises(100, 5))
def test_get_photos_by_album(api, albumid):
    r = api.GET(f'/photos', params={'albumId': albumid})
    assert r.ok
    validate_object(PhotosList, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_todos(api, userid):
    r = api.GET(f'/users/{userid}/todos')
    assert r.ok
    validate_object(TodosList, r.json())


@pytest.mark.parametrize('userid', choises(10, 5))
def test_get_todos_by_user(api, userid):
    r = api.GET(f'/todos/', params={'userId': userid})
    assert r.ok
    validate_object(TodosList, r.json())


@pytest.mark.parametrize('userid, status', [(-1, 201), (0, 201), (1, 201), (11, 201)])
def test_post_create(api, userid, status):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'title': 'foo', 'body': 'bar', 'userId': userid}
    r = api.POST('/posts', headers=headers, json=body)
    assert r.status_code == status
    if r.ok:
        validate_object(Post, r.json())


@pytest.mark.parametrize('postid, status', [(-1, 500), (0, 500), (1, 200), (101, 500)])
def test_post_update(api, postid, status):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'id': postid, 'title': 'foo', 'body': 'bar', 'userId': 1}
    r = api.PUT(f'/posts/{postid}', headers=headers, json=body)
    assert r.status_code == status
    if r.ok:
        validate_object(Post, r.json())


@pytest.mark.parametrize('postid, status', [(-1, 500), (0, 500), (1, 200), (101, 500)])
def test_post_patch(api, postid, status):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    body = {'title': 'foo'}
    r = api.PUT(f'/posts/{postid}', headers=headers, json=body)
    assert r.status_code == status
    if r.ok:
        assert r.json() == {'title': 'foo', 'id': postid}


@pytest.mark.parametrize('postid, status', [(-1, 200), (0, 200), (1, 200), (101, 200)])
def test_post_delete(api, postid, status):
    r = api.DELETE(f'/posts/{postid}')
    assert r.status_code == status
