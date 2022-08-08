# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install selenium
COPY . .
ENTRYPOINT ["python"]
CMD ["app.py"]
