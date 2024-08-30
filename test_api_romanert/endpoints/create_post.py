import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    post_id = None
    convert_to_json = None

    @allure.step('Create new post')
    def create_new_post(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url, json=body, headers=headers
        )
        self.convert_to_json = self.response.json()
        self.post_id = self.convert_to_json['id']
        return self.response
