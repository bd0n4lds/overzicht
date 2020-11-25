FROM python:3.6.5-alpine

COPY requirements.txt ./
COPY *.py ./
COPY *.yaml ./

RUN pip install --no-cache-dir -r requirements.txt && \
    chmod +x overzicht.py && \
    mkdir -p /var/log/overzicht

ENTRYPOINT ["python","overzicht.py"]