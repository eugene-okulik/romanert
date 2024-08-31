import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    response = None
    convert_to_json = None

    @allure.step('Delete object via DELETE method')
    def delete_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        self.convert_to_json = self.response.json()
        return self.response
