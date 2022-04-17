FROM python:3

COPY . /app

WORKDIR /app

EXPOSE 80

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--reload"]
