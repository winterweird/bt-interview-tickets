FROM python:3.12

RUN pip install --upgrade pip && pip install watchdog
COPY requirements.txt /requirements.txt
RUN pip-compile --output-file=/requirements.lock /requirements.txt && \
  pip install --no-cache-dir -r /requirements.lock

WORKDIR /app
