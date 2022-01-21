FROM python:3.8
WORKDIR /fastapi
COPY requirements.txt /fastapi
RUN pip3 install -r requirements.txt
COPY ./app /fastapi/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]