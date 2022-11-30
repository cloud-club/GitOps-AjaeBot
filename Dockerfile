#server image ubuntu 버전
FROM python:3.8-slim-buster
RUN apt-get update && apt-get install -y --no-install-recommends && rm -rf /var/lib/apt/lists/* \
python3-pip python3-dev build-essential \
pip install -r requirements.txt
COPY . /ajaebot-dockerfile
WORKDIR /ajaebot-dockerfile
CMD ["python3","Ajaebot_song.py"]
