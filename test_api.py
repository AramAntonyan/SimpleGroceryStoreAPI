import requests
import pytest



base_url = "https://simple-grocery-store-api.glitch.me/"
HTTP_code = 200

def test_get_status():
    response = requests.get(f'{base_url}status')
    print(response.status_code)
    assert response.status_code == HTTP_code, 'wrong status code'
    print((response.json()))

def test_get_all_products():
    response = requests.get(f"{base_url}products")
    assert response.status_code == HTTP_code, 'wrong status code'
    print(len(response.json()))
    assert len(response.json()) == 20, "actual length does not match to expected"


def test_get_single_product():
    productid = 4875
    response = requests.get(f'{base_url}products/{productid}')
    response_data = response.json()
    print(response_data)
    expected_keys = ['id', 'category', 'name', 'manufacturer',
                     'price', 'current-stock', 'inStock']
    for key in response_data.keys():
        assert key in expected_keys, 'wrong keys'
        print(key)




def test_create_new_cart():
    response = requests.post(f'{base_url}carts')
    print(response.status_code)
    assert response.status_code == 201, 'wrong code'
