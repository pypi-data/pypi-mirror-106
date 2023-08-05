FROM python:3.7
MAINTAINER oliverdding "oliverdding@tencent.com"
WORKDIR /app/restsqlserver/
ENTRYPOINT [ "python3", "main.py" ]
EXPOSE 8080
COPY ./requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
COPY . /app