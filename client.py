import argparse
import configparser
import dataclasses
import json
import http.client


conf = configparser.ConfigParser()
conf.read('config.ini')
client_conf = conf['CLIENT']

URL = client_conf['URL']
port = client_conf['port']
URN = client_conf['URN']


@dataclasses.dataclass
class Data:
    login: str
    password: str
    port: str
    URL: str
    URN: str


def login(data: Data) -> str:
    try:
        body = f'grant_type=&username={data.login}&password={data.password}&scope=&client_id=&client_secret='
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        conn = http.client.HTTPConnection(data.URL, port=int(data.port))
        conn.request('POST', data.URN, body, headers)
        res = conn.getresponse()
        return json.loads(res.read())['access_token']
    except Exception:
        return None


def get_info(data: Data, token: str):
        headers = {'accept': 'application/json', 'Authorization': f'Bearer {token}'}
        conn = http.client.HTTPConnection(data.URL, port=int(data.port))
        conn.request('GET', '/salary', headers=headers)
        res = conn.getresponse().read()
        try:
            return json.loads(res.read())
        except Exception:
            return res.decode('UTF-8')
            

def hide_token(token: str) -> str:
    try:
        return f'{token[:3]}...{token[-3:]}'
    except Exception:
        return None


parser = argparse.ArgumentParser()

parser.add_argument('login', nargs='?')
parser.add_argument('password', nargs='?')
parser.add_argument('--URL', default=URL)
parser.add_argument('--port', default=port)
parser.add_argument('--URN', default=URN)

args = parser.parse_args()

data = Data(login=args.login,
            password=args.password,
            URL=args.URL,
            port=args.port,
            URN=args.URN)

token = login(data)
if token:
    with open('temp', 'w') as store:
        store.write(token)

if data.login and data.password:
    print(f'You got auth token: {hide_token(token)}')
else:
    with open('temp', 'r') as store:
        print(get_info(data, store.read(token)))
