import csv

import requests
import json
import numpy as np
import pandas as pd
import random
import openpyxl

token ="SLACK_BOT_TOKEN"
channel ="#ajaebot"

def post_message(channel, text):
    # 본인이 발급받은 토큰값으로 대체
    SLACK_BOT_TOKEN = token
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + SLACK_BOT_TOKEN
    }
    payload = {
        'channel': channel,
        'text': text
    }
    r = requests.post('https://slack.com/api/chat.postMessage',
                      headers=headers,
                      data=json.dumps(payload)
                      )


def print_message():
    #파일 경로 설정
    Location = "."
    File ="Ajae.xlsx"

    # 추출 및 변환 코드
    #data_pd = pd.read_excel('{}/{}'.format(Location,File), header = None, index_col=None,names=None)
    #data_np = pd.DataFrame.to_numpy(data_pd)

    #이건 csv불러오는건데 일단 급한대로..
    data_pd = pd.read_csv("./Ajae.csv", header=None)
    data_np = pd.DataFrame.to_numpy(data_pd)

    # 추출 행, 열 선언
    #Row = len(data_np)
    Row = len(data_np)
    Column =1
    message = data_np[random.randint(0, Row-1),Column-1]

    return message

if __name__ == '__main__':
    #첫번째 param : 채널명 / 두번째 param : 메시지
    message = print_message()
    post_message("#ajaebot", message)