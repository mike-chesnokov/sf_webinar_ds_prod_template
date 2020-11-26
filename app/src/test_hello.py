import requests


def test_hello():
    params = ['', '42', 'python']
    for p in params:
        url = f'http://localhost:8000/hello?param={p}'
        res = requests.get(url)
        print(url)
        if res.status_code == 200:
            print(res.json())
            # assert res.status_code == 200, 'Not 200 status code'
            assert 'result' in res.json(), 'No field "result" in responce'
            assert 'param' in res.json(), 'No field "param" in responce'
            assert 'SERVER OK' in res.json()['result'], 'No "SERVER OK" in "result" field'
            assert p == res.json()['param'], '"param" field is not equal to input url obj_id'

            print('****SUCCESS****', '\n')
        else:
            print(res.status_code)
            print(res.text)
            print('****FAIL****', '\n')


if __name__ == '__main__':
    test_hello()
