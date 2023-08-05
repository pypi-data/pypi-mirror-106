import json
import os
import time

import requests
from notetool.tool.secret import read_secret
from wechatpy.enterprise import WeChatClient


class HuoBiMessage:
    def __init__(self, name='huobi', webhook=None, agent_id=None, secret=None, company_id=None):
        self.name = name
        # 机器人webhook
        self.webhook = read_secret("wechat", "notechats", "huobi", name, "webhook", value=webhook)
        # 应用ID
        self.agent_id = read_secret("wechat", "notechats", "huobi", name, "agent_id", value=agent_id)
        # 企业ID
        self.company_id = read_secret("wechat", "notechats", "huobi", name, "company_id", value=company_id)
        # 应用Secret
        self.secret = read_secret("wechat", "notechats", "huobi", name, "secret", value=secret)
        self.client = WeChatClient(corp_id=self.company_id, secret=self.secret)

    def send_msg(self, msg):
        self.check_token()
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        self.client.message.send(agent_id=self.agent_id, user_ids=['NiuLiangTao', 'GuoYe'], party_ids=['3'], msg=data)

        self.send_to_qywx(msg)

    def send_to_qywx(self, msg):
        headers = {'Content-Type': 'application/json'}
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }

        data = json.dumps(data)
        r = requests.post(url=self.webhook, headers=headers, data=data)

    def check_token(self):
        # 通行密钥
        access_token = None
        # 如果本地保存的有通行密钥且时间不超过两小时，就用本地的通行密钥
        if os.path.exists('ACCESS_TOKEN.txt'):
            txt_last_edit_time = os.stat('ACCESS_TOKEN.txt').st_mtime
            now_time = time.time()

            if now_time - txt_last_edit_time < 3600:  # 官方说通行密钥2小时刷新
                with open('ACCESS_TOKEN.txt', 'r') as f:
                    access_token = f.read()
                print('access_token:', access_token)
        # 如果不存在本地通行密钥，通过企业ID和应用Secret获取
        if not access_token:
            # r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.company_id}&corpsecret={self.secret}').json()
            # access_token = r["access_token"]
            access_token = self.client.fetch_access_token()
            print(access_token)
            # 保存通行密钥到本地ACCESS_TOKEN.txt
            with open('ACCESS_TOKEN.txt', 'w', encoding='utf-8') as f:
                f.write(access_token)

        self.client.session.set(self.client.access_token_key, access_token)
        return access_token
