import json

import requests
from requests import Response, PreparedRequest


class WeWork:
    def __init__(self):
        self.group_id=None
    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': 'wwd6da61649bd66fea',
                'corpsecret': 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
            }
        )
        self.token = r.json()['access_token']
        self.format(r)
        return r

    def tag_list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={
                'access_token': self.token
            }
        )

        self.format(r)
        return r

    def tag_add(self, name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={
                'access_token': self.token
            },
            json={
                "group_id": self.group_id,
                "group_name": "测试专用",
                'tag': [
                    {
                        'name': name
                    }
                ]
            }
        )

        self.format(r)
        self.group_id=r.json()['tag_group']['group_id']
        return r

    def tag_delete(self, id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={
                'access_token': self.token
            },
            json={
                'tag_id': [id]
            }
        )
        self.format(r)
        return r

    def format(self, res: Response):
        req: PreparedRequest = res.request
        print(req.url)
        print(req.body)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
