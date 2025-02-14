#
# Copyright (c) 2021 Matthew Penner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

FROM        --platform=$TARGETOS/$TARGETARCH eclipse-temurin:16-jdk-alpine


LABEL       author="Matthew Penner" maintainer="matthew@pterodactyl.io"

LABEL       org.opencontainers.image.source="https://github.com/pterodactyl/yolks"
LABEL       org.opencontainers.image.licenses=MIT

ENV DEBIAN_FRONTEND=noninteractive
ENV PS1="container@coldhost.eu~ "

RUN apk add --no-cache \
    lsof curl libcap ca-certificates openssl git tar sqlite fontconfig freetype tzdata iproute2 libstdc++ clamav clamav-daemon \
    && adduser -D -h /home/container container

RUN chown -R container:container /usr/bin/freshclam /var/lib/clamav

USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        ./../commit_count.txt /commit_count.txt
COPY        ./../commit_message.txt /commit_message.txt
COPY        ./../entrypoint.sh /entrypoint.sh
COPY        ./../freshclam.conf /freshclam.conf

CMD         [ "/bin/bash", "/entrypoint.sh" ]
