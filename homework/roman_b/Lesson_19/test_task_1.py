import requests
import pytest
import allure
from datetime import datetime


def assert_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        raise AssertionError("The datetime format is incorrect.")


@pytest.fixture(scope="session", autouse=True)
def start_end():
    print('Start Testing \n')
    yield
    print('\n -------- Testing completed')


@pytest.fixture(autouse=True)
def before_after_each():
    print('before test')
    yield
    print('\nafter test')


@pytest.fixture()
def new_object():
    header = {"content-type": "application/json"}
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=body, headers=header).json()
    new_id = response['id']
    yield new_id
    requests.delete(f"https://api.restful-api.dev/objects/{new_id}")


@allure.feature('Posts')
@allure.story('Create new object')
@allure.label('regression')
@pytest.mark.parametrize('bodies', [
    {"name": "Apple MacBook Pro 16",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook 15",
     "data": {"year": 2022, "price": 1149.99, "CPU model": "M1", "Hard disk size": "128 GB"}},
    {"name": "Apple MacBook Pro 14",
     "data": {"year": 2024, "price": 1649.99, "CPU model": "Intel Core i9", "Hard disk size": "512 GB"}}
])
def test_create_object(bodies):
    header = {"content-type": "application/json"}
    body = bodies
    with allure.step('Send a POST request'):
        response = requests.post("https://api.restful-api.dev/objects", json=body, headers=header).json()
    date = response['createdAt']
    assert_date(date)


@allure.feature('Posts')
@allure.story('Modify object with put method')
@allure.label('regression')
@pytest.mark.medium
def test_modify_object_put(new_object):
    with allure.step('Send data(body and header) for put request'):
        header = {"content-type": "application/json"}
        body = {
            "name": "Updated Apple MacBook Pro 16",
            "data": {
                "year": 2020,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }
    with allure.step(f'Run put request'):
        response = requests.put(f"https://api.restful-api.dev/objects/{new_object}", json=body, headers=header)
    assert response.status_code == 200
    assert response.json()['name'] == "Updated Apple MacBook Pro 16"


@allure.feature('Posts')
@allure.story('Modify object with patch method')
@allure.label('regression')
@pytest.mark.critical
def test_modify_object_patch(new_object):
    header = {"content-type": "application/json"}
    body = {"name": "Apple MacBook Pro 16 (Updated Name)"}
    response = requests.patch(f"https://api.restful-api.dev/objects/{new_object}", json=body, headers=header)
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro 16 (Updated Name)'


@allure.feature('Posts')
@allure.story('Delete object')
@allure.label('regression')
def test_delete_obj(new_object):
    response = requests.delete(f"https://api.restful-api.dev/objects/{new_object}")
    assert response.status_code == 200
    response = requests.delete(f"https://api.restful-api.dev/objects/{new_object}")
    assert response.status_code == 404
