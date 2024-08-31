import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None
    convert_to_json = None

    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url, json=body, headers=headers
        )
        self.convert_to_json = self.response.json()
        self.object_id = self.convert_to_json['id']
        return self.response
