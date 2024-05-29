import requests
from my_shop_project_test.utils.allure_attach import response_logging, response_attaching

base_api_url = 'https://api.my-shop.ru/cgi-bin'


def api_request(endpoint, method, data=None, params=None, headers=None):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method, url, data=data, params=params, headers=headers)
    response_logging(response)
    response_attaching(response)
    return response
