import pytest


@pytest.mark.parametrize('bodies', [
    {"name": "Apple MacBook Pro 16",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook 15",
     "data": {"year": 2022, "price": 1149.99, "CPU model": "M1", "Hard disk size": "128 GB"}},
    {"name": "Apple MacBook Pro 14",
     "data": {"year": 2024, "price": 1649.99, "CPU model": "Intel Core i9", "Hard disk size": "512 GB"}}
])
def test_new_object(create_post_endpoint, bodies):
    create_post_endpoint.create_new_post(body=bodies)
    create_post_endpoint.check_response_title_is_correct(bodies['name'])


def test_modify_object_put(update_post_put_endpoint, create_post_endpoint):
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
    update_post_put_endpoint.update_post_put(post_id=create_post_endpoint.post_id, body=body)
    update_post_put_endpoint.check_response_title_is_correct(body['name'])
    update_post_put_endpoint.check_that_status_is_200()


def test_modify_object_patch(update_post_patch_endpoint, create_post_endpoint):
    body = {"name": "Apple MacBook Pro 16 (Updated Name)"}
    update_post_patch_endpoint.update_post_patch(post_id=create_post_endpoint.post_id, body=body)


def test_delete_object(delete_post_endpoint, create_post_endpoint):
    delete_post_endpoint.delete_post(post_id=create_post_endpoint.post_id)
