FROM ubuntu
MAINTAINER seu@soueu.com

RUN apt-get update \
    && apt-get install -y nginx \
    && apt-get clean


COPY index.html /var/www/html

ENV ricardo lindo

VOLUME /var/www/html

CMD /usr/sbin/nginx -g 'daemon off;'

EXPOSE 80
