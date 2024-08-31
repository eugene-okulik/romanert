import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Verify title is correct')
    def check_response_title_is_correct(self, name):
        assert self.response.json()['name'] == name

    @allure.step('Verify response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Verify error 404 received (negative scenario)')
    def check_bad_request(self):
        assert self.response.status_code == 404
