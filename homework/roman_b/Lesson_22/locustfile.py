from locust import task, HttpUser
import random


class ObjectManipulation(HttpUser):
    new_id = None

    def on_start(self):
        try:
            response = self.client.post('/objects', json={
                "name": "Apple MacBook Pro 16",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }})
            self.new_id = response.json().get('id')
        except Exception as e:
            print(f"Failed to create object: {str(e)}")

    @task(1)
    def test_create_object(self):
        self.client.post('/objects', headers={'Content-type': 'application/json'},
                         json={random.choice([
                             {"name": "Apple MacBook Pro 16",
                              "data": {"year": 2019, "price": 1849.99,
                                       "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
                             {"name": "Apple MacBook 15",
                              "data": {"year": 2022, "price": 1149.99,
                                       "CPU model": "M1", "Hard disk size": "128 GB"}},
                             {"name": "Apple MacBook Pro 14",
                              "data": {"year": 2024, "price": 1649.99,
                                       "CPU model": "Intel Core i9", "Hard disk size": "512 GB"}}
                         ])})

    @task(3)
    def get_all_objects(self):
        self.client.get('/objects', headers={'Content-type': 'application/json'})

    @task(2)
    def test_modify_object_put(self):
        self.client.put(f'objects/{self.new_id}', headers={'Content-type': 'application/json'},
                        json={
                            "name": "Updated Apple MacBook Pro 16",
                            "data": {
                                "year": 2020,
                                "price": 2049.99,
                                "CPU model": "Intel Core i9",
                                "Hard disk size": "1 TB",
                                "color": "silver"
                            }})

    @task(2)
    def test_modify_object_patch(self):
        self.client.patch(f'objects/{self.new_id}', headers={'Content-type': 'application/json'},
                          json={"name": "Apple MacBook Pro 16 (Updated Name)"})

    @task(1)
    def test_delete_obj(self):
        if self.new_id:
            self.client.delete(f'objects/{self.new_id}')
