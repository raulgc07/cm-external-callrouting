FROM python:3.8.17-alpine3.18
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["gunicorn" , "-b", "0.0.0.0:8000", "app:app"]