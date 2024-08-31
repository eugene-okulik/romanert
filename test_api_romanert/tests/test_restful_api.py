import pytest


@pytest.mark.parametrize('bodies', [
    {"name": "Apple MacBook Pro 16",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook 15",
     "data": {"year": 2022, "price": 1149.99, "CPU model": "M1", "Hard disk size": "128 GB"}},
    {"name": "Apple MacBook Pro 14",
     "data": {"year": 2024, "price": 1649.99, "CPU model": "Intel Core i9", "Hard disk size": "512 GB"}}
])
def test_new_object(create_object_endpoint, bodies):
    create_object_endpoint.create_new_object(body=bodies)
    create_object_endpoint.check_response_title_is_correct(bodies['name'])


def test_modify_object_put(update_object_put_endpoint, new_object_id):
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
    update_object_put_endpoint.update_object_put(new_object_id, body)
    update_object_put_endpoint.check_response_title_is_correct(body["name"])
    update_object_put_endpoint.check_that_status_is_200()


def test_modify_object_patch(update_object_patch_endpoint, new_object_id):
    body = {"name": "Apple MacBook Pro 16 (Updated Name)"}
    update_object_patch_endpoint.update_object_patch(object_id=new_object_id, body=body)
    update_object_patch_endpoint.check_that_status_is_200()
    update_object_patch_endpoint.check_response_title_is_correct(body["name"])


def test_delete_object(delete_object_endpoint, new_object_id):
    delete_object_endpoint.delete_object(object_id=new_object_id)
    delete_object_endpoint.check_that_status_is_200()
    delete_object_endpoint.delete_object(object_id=new_object_id)
    delete_object_endpoint.check_bad_request()
