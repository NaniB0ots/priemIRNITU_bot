# pull official base image
FROM python:3.9


# set work directory
RUN mkdir -p /usr/src/web/
WORKDIR /usr/src/web/

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY run.sh .

# copy project
COPY . .
RUN pip install -r requirements.txt


EXPOSE 8080

RUN chmod +x run.sh

# run entrypoint.sh
CMD ["./run.sh"]

