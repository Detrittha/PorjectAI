FROM python:3.11

WORKDIR /con2

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /con2/requirements.txt

COPY ./app /con2/app

ENV PYTHONPATH "${PYTHONPATH}:/con2"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]