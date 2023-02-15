FROM python:3.10-bullseye

RUN mkdir /code
WORKDIR /code

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY cafe_menu_backend cafe_menu_backend/
# COPY migrations migrations/

EXPOSE 5000
