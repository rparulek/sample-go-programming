FROM ubuntu:latest
ENV endpoint default_value
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install requests flask flask-jsonpify flask-sqlalchemy flask-restful
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python ${endpoint}.py"]
