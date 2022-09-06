FROM python:3.7
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./creativity /code/creativity
WORKDIR /code/
EXPOSE 8000
CMD ["uvicorn", "creativity.app:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--workers", "2"]