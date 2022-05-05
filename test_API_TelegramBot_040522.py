import requests
from pprint import pprint
import datetime

class TestTelegramBot:
    def __init__(self, token: str):
        self.token = token

    def read_token(self, file_name='token_tlg.txt'):
        with open(file_name, 'r', encoding='utf-8') as token_file:
            token = token_file.read().strip()
            print(token)
        return token

    def test_token(self, method='getMe'):
        self.token = TestTelegramBot.read_token(TestTelegramBot)
        URL = f'https://api.telegram.org/bot{self.token}/{method}'
        resp = requests.get(url=URL)
        resp = resp.json()
        pprint(resp)
        return resp

    def test_update(self, method='getUpdates'):
        self.token = TestTelegramBot.read_token(TestTelegramBot)
        URL = f'https://api.telegram.org/bot{self.token}/{method}'
        resp = requests.get(url=URL)
        resp = resp.json()
        pprint(resp)
        return resp

    def test_chat_id(self, method='chat'):
        self.token = TestTelegramBot.read_token(TestTelegramBot)
        URL = f'https://api.telegram.org/bot{self.token}/{method}'
        resp = requests.get(url=URL)
        resp = resp.json()
        pprint(resp)
        return resp


    def send_message(self, method='sendMessage', text_message=f"How do you do now? Today {datetime.datetime.now()}."):
        self.token = TestTelegramBot.read_token(TestTelegramBot)
        URL = f'https://api.telegram.org/bot{self.token}/{method}?'
        PARAMS = {
            'chat_id' : '5024094511',
            'text' : text_message
        }
        resp = requests.get(url=URL, params=PARAMS)
        resp = resp.json()
        pprint(resp)
        return resp



if __name__ == '__main__':
    # TestTelegramBot.test_update(TestTelegramBot)
    # TestTelegramBot.test_token(TestTelegramBot)
    # TestTelegramBot.read_token(TestTelegramBot)
    TestTelegramBot.send_message(TestTelegramBot)