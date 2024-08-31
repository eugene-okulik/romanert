import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_put_endpoint():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_patch_endpoint():
    return UpdateObjectPatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def new_object_id(create_object_endpoint):
    body = {
        "name": "Apple MacBook Pro 14",
        "data": {
           "year": 2019,
           "price": 1849.99,
           "CPU model": "Intel Core i9",
           "Hard disk size": "1 TB"
        }
    }
    create_object_endpoint.create_new_object(body)
    yield create_object_endpoint.object_id
