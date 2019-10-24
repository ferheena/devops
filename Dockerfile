FROM python:2.7

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app/app.py .

EXPOSE 5000

CMD ["python", "app.py"]

