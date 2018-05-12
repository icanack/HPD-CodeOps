FROM centos

MAINTAINER icanack@gmail.com

RUN yum update && yum install install -y httpd 

ENV APACHE_RUN_USER apache
ENV APACHE_RUN_GROUP apache
ENV APACHE_LOG_DIR /var/log/httpd
ENV APACHE_LOCK_DIR /var/lock/httpd
ENV APACHE_PID_FILE /var/run/httpd.pid

RUN mkdir -p $APACHE_LOG_DIR $APACHE_LOCK_DIR $APACHE_PID_FILE 

LABEL app minha_app

ADD index.html /var/www/html


VOLUME /var/www/html



WORKDIR /var/www/html

ENTRYPOINT ["/usr/sbin/httpd","-D", "FOREGROUND"]




EXPOSE 80
