import json

import requests


class WeWork:
    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': 'wwd6da61649bd66fea',
                'corpsecret': 'heLiPlmyblHRiKAgGWZky4-KdWqu1V22FeoFex8RfM0'
            }
        )
        self.token = r.json()['access_token']
        self.format(r.json())
        return r

    def tag_list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={
                'access_token': self.token
            }
        )

        self.format(r.json())
        return r
    def tag_add(self, name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={
                'access_token': self.token
            },
            json={
                "group_name": "测试专用",
                'tag': [
                    {
                        'name': name
                    }
                ]
            }
        )
        self.format(r.json())
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
        self.format(r.json())
        return r

    def format(self, data):
        print(json.dumps(data, indent=2, ensure_ascii=False))

