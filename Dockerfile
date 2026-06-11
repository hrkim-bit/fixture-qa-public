FROM python:latest

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
ENV DB_PASSWORD="Pa55w0rd!"
ENV SECRET_KEY="django-insecure-do-not-use-0000000000"

EXPOSE 5000
CMD ["python", "app.py"]
