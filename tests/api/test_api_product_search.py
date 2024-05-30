import pytest
import allure
import jsonschema
from my_shop_project_test.helper.load_schema import load_schema
from my_shop_project_test.helper.api_requests import api_request


@allure.epic('API. Search')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking the product search on the main page")
@allure.label('microservice', 'API')
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
@pytest.mark.api
def test_successful_searching_of_product_by_title():
    schema = load_schema('successful_searching_product.json')

    with allure.step("Send request for successful search"):
        product_title = 'Python для детей. Самоучитель по программированию'
        url = f"/ajax/search.pl"
        params = {
            "term": product_title
        }
        headers = {"Content-Type": "application/json"}
        result = api_request(endpoint=url, method='GET', params=params, headers=headers)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert 'python для детей самоучитель по программированию' in result.json()['suggest'][0]['value']


@allure.epic('API. Search')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking the product search on the main page")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_unsuccessful_searching_of_product_by_title():
    schema = load_schema('unsuccessful_searching_product.json')

    with allure.step("Send request for unsuccessful search"):
        product_title = 'asddfgrhtjykykk'
        url = f"/ajax/search.pl"
        params = {
            "term": product_title
        }
        headers = {"Content-Type": "application/json"}
        result = api_request(endpoint=url, method='GET', params=params, headers=headers)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert product_title in result.json()['suggest'][0]['value']

