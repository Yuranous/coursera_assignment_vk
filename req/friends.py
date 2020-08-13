import requests

ACCESS_TOKEN = '5069c2ec5069c2ec5069c2ec29501ab2d8550695069c2ec0f5dd02610497c670b07ba29'
API_VERSION = '5.71'
CURRENT_YEAR = 2020


def calc_age(uid):
    params = {'access_token': ACCESS_TOKEN, 'user_ids': uid, 'v': API_VERSION}
    request_user = requests.get('https://api.vk.com/method/users.get', params=params)
    del params['user_ids']
    params['user_id'] = request_user.json()['response'][0]['id']
    params['fields'] = 'bdate'
    request_friends = requests.get('https://api.vk.com/method/friends.get', params=params)
    friends_age = dict()
    for friend in request_friends.json()['response']['items']:
        try:
            bd = friend['bdate']
            age = CURRENT_YEAR - int(bd.split('.')[2])
            if age in friends_age.keys():
                friends_age[age] += 1
            else:
                friends_age[age] = 1
        except (IndexError, KeyError) as e:
            pass
    result = friends_age.items()
    result = sorted(result, key=lambda x: (-x[1], x[0]))
    return result


if __name__ == '__main__':
    res = calc_age(98372975)
    print(res)
    # pass
