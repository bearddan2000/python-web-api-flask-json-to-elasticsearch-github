
FROM python:latest

COPY bin/ /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "app.py"]