import requests


def test_api_if_else():
    res = requests.get('https://scotch.io')
    if res:
        print('\nSo OK')
    else:
        print('So NOT ok')
    print(res)


def test_api_status():
    res = requests.get('https://scotch.io')
    print('\n', res)


# def test_api_get_text():
#     res = requests.get('https://scotch.io')
#     print('\n', res.text)


def test_api_get_but_use_server_translate_func():
    res = requests.get('https://scotch.io')
    print(res)


def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200


