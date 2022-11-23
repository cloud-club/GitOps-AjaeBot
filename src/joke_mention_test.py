import os
import time
import re
import random
import pandas as pd
from slackclient import SlackClient



slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
starterbot_id = None

# constants
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM
EXAMPLE_COMMAND = "심심해"
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"


def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:  # message type의 이벤트에서만 command 찾는다.
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:  # 멘션된 userID와 이전에 저장한 bot의 아이디가 같을 경우
                return message, event["channel"]  # ChannelID와 message return
    return None, None


def parse_direct_mention(message_text):
    """
        text의 시작부분에서 @멘션을 찾고, 멘션된 것의 userID를 return 한다.
        @멘션이 없을 경우 None return
    """
    matches = re.search(MENTION_REGEX, message_text)  # @멘션으로 시작한 경우
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def handle_command(command, channel):
    """
       멘션됐을 경우 return 될 command를 생성하는 함수
    """
    # 지정된 명령어로 호출되지 않았을 경우 return 할 default response
    default_response = "Not sure what you mean. Try *{}*.".format(EXAMPLE_COMMAND)

    response = None
    # 아재 개그 추출 함수 넣기 !!
    if command.startswith(EXAMPLE_COMMAND):  # do로 시작하는 경우?
        response = print_message()

    # channel에 메세지 보내기
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response or default_response
    )


# 엑셀에서 개그 추출하는 함수
def print_message():
    # 파일 경로 설정
    #Location = "."
    #File = "Ajae.xlsx"



    # 추출 및 변환 코드
    #data_pd = pd.read_excel('{}/{}'.format(Location, File), header=None, index_col=None, names=None)

    # 이건 csv불러오는건데 일단 급한대로..
    data_pd = pd.read_csv("./Ajae.csv", header=None)
    data_np = pd.DataFrame.to_numpy(data_pd)

    # 추출 행, 열 선언
    Row = len(data_np)
    Column = 1
    message = data_np[random.randint(0, Row), Column - 1]

    return message


if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Web API method `auth.test` 통해 bot의 user ID를 읽어온다.
        # slackBot은 slack APP 이 설치된 workspace 마다 UserID 를 가진다.
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())  # 이벤트가 해당 Bot을 호출하는 command를 포함하는지 확인
            if command:
                handle_command(command, channel)  # 호출될 경우 무엇을 할지 결정하는 함수
            time.sleep(RTM_READ_DELAY)
    else:
        print(os.environ.get('SLACK_BOT_TOKEN'))  # 환경변수 설정 확인
        print("Connection failed. Exception traceback printed above.")