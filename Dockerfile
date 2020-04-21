FROM baalajimaestro/userbot_python:latest

ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN git clone https://aad6d88b1fafada99def7111c1a2a6e663185f12@github.com/Ayush1311/PAPERPLANE-REBORN.git -b master /app
RUN
pip install --upgrade -r requirements.txt

#
# Copies session and config(if it exists)
#
COPY ./userbot.session ./config.env* ./client_secrets.json* ./secret.json* /app/

#
# Finalization
#
CMD ["bash","init/start.sh"]
