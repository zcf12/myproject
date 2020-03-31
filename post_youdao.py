import requests

url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"


def get_salt():
    return '15846862626819'


def get_sign():
    return 'b6ca26b2024cf4badffbb2baec27833f'


def get_ts():
    import time
    t = time.time()
    ts = str(int(round(t * 1000)))
    return ts


form_data={
    'i':'我和你都是中国',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': get_salt(),
    'sign': get_sign(),
    'ts': get_ts(),
    'bv': 'ec579abcd509567b8d56407a80835950',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
response=requests.post(url,form_data)
print(response.text)
