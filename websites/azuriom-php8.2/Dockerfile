FROM php:8.2-fpm-alpine

LABEL       org.opencontainers.image.source="https://github.com/Coldhost/yolks"

USER        container
ENV         USER=container HOME=/home/container
WORKDIR     /home/container

COPY        ./../entrypoint.sh /entrypoint.sh
CMD         [ "/bin/ash", "/entrypoint.sh" ]
