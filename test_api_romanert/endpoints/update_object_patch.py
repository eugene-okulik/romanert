import requests
import allure
from test_api_romanert.endpoints.endpoint import Endpoint


class UpdateObjectPatch(Endpoint):
    response = None
    convert_to_json = None

    @allure.step('Update object via PATCH method')
    def update_object_patch(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}', json=body, headers=headers
        )
        self.convert_to_json = self.response.json()
        return self.response
