import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    convert_to_json = None
    headers = {'Content-type': 'application/json'}

    @allure.step('Verify title is correct')
    def check_response_title_is_correct(self, title):
        assert self.convert_to_json['name'] == title

    @allure.step('Verify response is 200')
    def check_that_status_is_200(self):
        try:
            assert self.response.status == 200
        except ValueError:
            print(self.response.status)

    @allure.step('Verify error 400 received (negative scenario)')
    def check_bad_request(self):
        assert self.response.status_code == 400
