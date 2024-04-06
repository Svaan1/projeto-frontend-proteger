FROM python:3.11.4

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

COPY ./src backend/src

EXPOSE 8080

CMD ["uvicorn", "backend.src.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]