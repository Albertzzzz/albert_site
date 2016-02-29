FROM django:1.0

MAINTAINER albert albert.zhang0602@gmail.com

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python","manage.py","runserver","0.0.0.0:8010"]
