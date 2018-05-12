FROM ubuntu

MAINTAINER icanack@gmail.com

RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP ww-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

RUN mkdir -p $APACHE_LOG_DIR $APACHE_LOCK_DIR $APACHE_PID_FILE 

LABEL app minha_app

ADD index.html /var/www/html


VOLUME /var/www/html



WORKDIR /var/www/html

ENTRYPOINT ["/usr/sbin/apache2","-D", "FOREGROUND"]




EXPOSE 80
