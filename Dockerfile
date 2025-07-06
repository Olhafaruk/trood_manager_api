FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:/app/backend"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*


COPY wait-for-db.sh .
COPY entrypoint.sh .

RUN chmod +x wait-for-db.sh entrypoint.sh
CMD ["./entrypoint.sh"]

