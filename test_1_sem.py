import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

S = requests.Session()

''' POST '''

def test_step1(user_login, get_description):
    res = S.post(url=data['address_post'], headers={'X-Auth-Token': user_login},
                 data={'title': data['title'], 'description': data['description'], 'content': ['content']})
    assert res.status_code == 200, 'post_create FAIL'

''' GET '''
def test_step2(user_login, get_description):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    list_description = [i['description'] for i in result]
    assert get_description in list_description, 'check_post_create FAIL'

''' DELETE '''

def test_step3(user_login):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    res = S.delete(url=data['address_post'] + '/' + str(result[0]['id']), headers={'X-Auth-Token': user_login})
    assert res.status_code == 200, 'post_delete FAIL'

''' CHECK DELETE '''

def test_step4(user_login, get_description):
    result = S.get(url=data['address'], headers={'X-Auth-Token': user_login}).json()['data']
    list_description = [i['description'] for i in result]
    assert get_description not in list_description, 'check_post_create FAIL'