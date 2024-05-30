import pytest
import allure
import jsonschema
from my_shop_project_test.helper.load_schema import load_schema
from my_shop_project_test.helper.api_requests import api_request


@allure.epic('API. Add product to favorites')
@allure.label("owner", "Violin88-tech")
@allure.feature("Checking whether a product has been added to favorites")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
@pytest.mark.api
def test_adding_product_to_favorite():
    schema = load_schema('successful_adding_product_to_favorite.json')

    with allure.step("Send a request to add a product to favorites"):
        url = f"/shop2.pl"
        params = {
            "q": "add_cart",
            "quantity": 1,
            "product_id": 4913578,
            "save": 1
        }
        data = {"quantity": 1}
        headers = {"Content-Type": "application/json"}
        result = api_request(endpoint=url, method='PUT', params=params, headers=headers, data=data)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()['save']['4913578'] == '1'
        assert result.json()['total']['quantity'] == 0


@allure.epic('API. Get data about product in favorite')
@allure.label("owner", "MaryMokretsova")
@allure.feature("Checking a product in favorite")
@allure.tag('regress', 'api', 'normal')
@allure.severity('normal')
@allure.label('layer', 'api')
def test_info_product_in_favorite():
    schema = load_schema('get_info_product_in_favorite.json')

    with allure.step("Send a request to receive your favorite products"):
        url = f"/shop2.pl"
        params = {
            "q": "cart"
        }
        headers = {"Content-Type": "application/json"}
        result = api_request(endpoint=url, method='PUT', params=params, headers=headers)

    with allure.step("Checking the answer"):
        assert result.status_code == 200
        jsonschema.validate(result.json(), schema)
        assert result.json()['save'] == []
        assert result.json()['cart'] == []