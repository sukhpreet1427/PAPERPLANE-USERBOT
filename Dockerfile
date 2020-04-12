FROM baalajimaestro/userbot_python:latest

ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN git clone https://Ayush1311:Ayushtheman@2003@github.com/PAPERPLANE-REBORN.git -b master /app

#
# Copies session and config(if it exists)
#
COPY ./userbot.session ./config.env* ./client_secrets.json* ./secret.json* /app/

#
# Finalization
#
CMD ["bash","init/start.sh"]
