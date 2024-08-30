import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    response = None
    convert_to_json = None

    @allure.step('Delete post via DELETE method')
    def delete_post(self, post_id):
        self.response = requests.delete(f'{self.url}/{post_id}')
        self.convert_to_json = self.response.json()
        return self.response
