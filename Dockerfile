# 태그명 생략해 ubuntu 최신 버전(Latest) 기반 이미지 제작
FROM python:3.8-slim-buster
MAINTAINER juya "kjy2967@naver.com"
# Docker 이미지 내부에서 RUN,CMD,ENTRYPOINT 의 명령이 실행될 dir 설정
WORKDIR /ajaeBot-docker/app
# host 내부 파일 전부 container의 WORKDIR 내부에 복사
COPY . ./

RUN pip3 install -r requirements.txt
# slackbot token 환경 변수 설정
ENV SLACK_BOT_TOKEN=.
CMD ["python3","joke_mention_test.py"]