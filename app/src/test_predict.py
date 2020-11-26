import requests


def test_predict():
    params = ['8740', '162', '', 'python', '-1', '168']
    responses = {
        '8740': {'obj_id': '8740', 'prediction': 2.478, 'response_status': 'OK'},
        '162': {'obj_id': '162', 'prediction': 2.4255, 'response_status': 'OK'},
        '': {'obj_id': '', 'prediction': -1, 'response_status': 'ERROR'},
        'python': {'obj_id': 'python', 'prediction': -1, 'response_status': 'ERROR'},
        '-1': {'obj_id': '-1', 'prediction': -1, 'response_status': 'ERROR'},
        '168': {'obj_id': '168', 'prediction': -1, 'response_status': 'ERROR'}
    }
    for p in params:
        url = f'http://localhost:8000/predict?obj_id={p}'
        res = requests.get(url)
        print(url)
        if res.status_code == 200:
            print(res.json())

            assert 'prediction' in res.json(), 'No field "prediction" in responce'
            assert 'obj_id' in res.json(), 'No field "obj_id" in responce'
            assert 'response_status' in res.json(), 'No field "response_status" in responce'
            assert p == res.json()['obj_id'], '"obj_id" field is not equal to input url obj_id'

            assert responses[p]['obj_id'] == res.json()['obj_id'], 'obj_id mismatch'
            assert responses[p]['prediction'] == res.json()['prediction'], 'Prediction mismatch'
            assert responses[p]['response_status'] == res.json()['response_status'], 'Response_status mismatch'

            print('****SUCCESS****', '\n')
        else:
            print(res.status_code)
            print(res.text)
            print('****FAIL****', '\n')


if __name__ == '__main__':
    test_predict()
