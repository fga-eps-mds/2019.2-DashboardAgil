FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN pip install -r requirements.txt && \
    chmod +x boot.sh

CMD ["./boot.sh"]