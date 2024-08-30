import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class UpdatePostPut(Endpoint):
    response = None
    convert_to_json = None

    @allure.step('Update post via PUT method')
    def update_post_put(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}', json=body, headers=headers
        )
        self.convert_to_json = self.response.json()
        return self.response
