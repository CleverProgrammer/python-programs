import requests

locu_api = '2d40e5a0c19390618e88f8dbff61cc50ec4e8a8b'


def locu_search(city='', state=''):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = city.replace(' ', '%20')
    if state and city:
        final_url = url + '&locality=' + locality + '&region=' + state
    elif state:
        final_url = url + '&region=' + state
    else:
        final_url = url + '&locality=' + locality
    r = requests.get(final_url)
    data = r.json()
    for item in data['objects']:
        print(item['name'], item['phone'])
