import requests


class TestHttp:
    def test_get(self):
        r = requests.get(
            "https://httpbin.testing-studio.com/get",
            params={'a': 1, 'b': '霍格沃兹测试学院'}
        )
        print(r.status_code)
        print(r.encoding)
        print(r.content)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        r=requests.post(
            'https://httpbin.testing-studio.com/post',
            data={"custtel": '15600534760'}
        )
        print(r.text)
        assert r.status_code == 200
        # assert r.json()['url'] == 'https://httpbin.testing-studio.com/post'
        assert r.json()['form']['custtel'] == '15600534760'
