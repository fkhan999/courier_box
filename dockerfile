# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8000
WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]