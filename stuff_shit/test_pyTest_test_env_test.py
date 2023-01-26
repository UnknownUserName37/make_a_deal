import pytest
import requests


@pytest.mark.swof
def test_post():
    params = {'key1': 'value1', 'key2': 'value2'}
    resp = requests.get('https://httpbin.org/post')
    print(resp.url)


# @pytest.mark.my_first_conscious_fixture_using
def test_get_code():
    resp = requests.get('https://httpbin.org/get')
# статус ответа сервера pytest --version   # показывает версию и место, откуда импортирован ``pytest``
    print(resp.status_code)


# @pytest.mark.my_first_conscious_fixture_using
def test_testa():
    resp = requests.get('https://httpbin.org/')
# статус ответа сервера
    print(resp.encoding)


# @pytest.mark.swof
# def test_get_after_post():
#     sess = Session()
#     req = Request('GET', 'https://httpbin.org')
#     prepped = sess.prepare_request(req)
# # Слияние параметров переменной среды в сеанс/сессию
#     settings = sess.merge_environment_settings(prepped.url, {}, None, None, None)
#     resp = sess.send(prepped, **settings)
#     print(resp.status_code)

