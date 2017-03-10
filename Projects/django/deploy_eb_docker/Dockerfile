FROM        eb-base
MAINTAINER  dev@azelf.com

#RUN         apt-get -y update
#RUN         apt-get -y install python3
#RUN         apt-get -y install python3-pip
#RUN         apt-get -y install nginx

COPY        . /srv/app
WORKDIR     /srv/app

#RUN         pip3 install -r requirements.txt
#RUN         pip3 install uwsgi

COPY        .conf-secret/uwsgi-app.ini /etc/uwsgi/sites/app.ini
