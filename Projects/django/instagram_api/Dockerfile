FROM        ubuntu:16.04
MAINTAINER  dev@azelf.com

RUN         apt-get -y update
RUN         apt-get -y install python3
RUN         apt-get -y install python3-pip
RUN         apt-get -y install nginx
RUN         apt-get -y install supervisor

RUN         pip3 install django
RUN         pip3 install uwsgi

COPY        . /srv/app
WORKDIR     /srv/app
RUN         pip3 install -r requirements.txt

COPY        .conf/uwsgi-app.ini         /etc/uwsgi/sites/app.ini
COPY        .conf/nginx.conf            /etc/nginx/nginx.conf
COPY        .conf/nginx-app.conf        /etc/nginx/sites-available/app.conf
COPY        .conf/supervisor-app.conf   /etc/supervisor/conf.d/
RUN         ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf

EXPOSE      4040

#CMD         supervisord -n