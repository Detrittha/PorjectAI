FROM python:3.11

WORKDIR /aiproject

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /aiproject/requirements.txt

COPY ./app /aiproject/app
COPY ./model /aiproject/model

ENV PYTHONPATH "${PYTHONPATH}:/aiproject"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]