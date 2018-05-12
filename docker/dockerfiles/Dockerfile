FROM ubuntu:16.04
MAINTAINER Ricardo <icanack@gmail.com>

RUN apt-get update \
    && apt-get install -y nginx \
    && apt-get clean

COPY html/index.html /var/www/html/



ENV abacate verde

VOLUME /var/www/html

EXPOSE 80

#ENTRYPOINT ["/usr/sbin/nginx"]

#CMD ["-g", "daemon off;"]

CMD /usr/sbin/nginx -g 'daemon off;'
