import json

import pytest
import requests

from test_http.wework import WeWork


class TestWeWork:
    @classmethod
    def setup_class(cls):
        cls.wework = WeWork()
        r = cls.wework.get_token()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        # done: clear all the test data
        r = cls.wework.tag_list()
        tags = [tag for group in r.json()['tag_group'] for tag in group['tag']]

        for tag in tags:
            id = tag['id']
            r = cls.wework.tag_delete(id)

        #bug： 企业微信后台使用了负载均衡，数据不同步。相同的groupname可能会出现多个tag group
        cls.wework.tag_add("demo")



    def test_tag_list(self):
        r = self.wework.tag_list()
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize("name", [
        "中文", 'english', 'a_b', 'a-b', ' '
        # todo: more test data
    ])
    def test_tag_add(self, name):
        r = self.wework.tag_add(name)
        assert r.json()['errcode'] == 0
        r = self.wework.tag_list()
        tags = [tag for group in r.json()['tag_group'] for tag in group['tag'] if tag['name'] == name]
        print(tags)
        assert len(tags) == 1

    def test_tag_delete(self):
        name = "demo05"
        r = self.wework.tag_add(name)
        r = self.wework.tag_list()
        assert r.json()['errcode'] == 0
        ids = [tag['id'] for group in r.json()['tag_group'] for tag in group['tag'] if tag['name'] == name]
        # 删除标签
        r = self.wework.tag_delete(ids[0])
        assert r.json()['errcode'] == 0
