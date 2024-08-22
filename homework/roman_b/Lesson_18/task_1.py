import requests
from datetime import datetime


def assert_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f%z')
    except ValueError:
        raise AssertionError("The datetime format is incorrect.")


def create_object():
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
    date = response['createdAt']
    assert_date(date)
    print(response)
    return response['id']


def modify_object_put(object_id):
    header = {"content-type": "application/json"}
    body = {
       "name": "Apple MacBook Pro 16",
       "data": {
          "year": 2019,
          "price": 2049.99,
          "CPU model": "Intel Core i9",
          "Hard disk size": "1 TB",
          "color": "silver"
       }
    }

    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json=body, headers=header)
    assert response.status_code == 200, "Status code not 200"
    print(response.json())


def modify_object_patch(object_id):
    header = {"content-type": "application/json"}
    body = {
       "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json=body, headers=header)
    assert response.status_code == 200, "Status code not 200"
    assert response.json()['name'] == 'Apple MacBook Pro 16 (Updated Name)'
    print(response.json())


def delete_object(object_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code == 200, "Status code not 200"
    print(response)


created_id = create_object()
modify_object_put(created_id)
modify_object_patch(created_id)
delete_object(created_id)
