FROM python:3.11

LABEL maintainer="Reza Teymouri Nejad <rezatn0934@gmail.com>"

LABEL description="Dockerfile for a Python application using Python 3.11"

LABEL version="1.0"

LABEL source="https://github.com/rezatn0934/OnlineShop.git"

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
