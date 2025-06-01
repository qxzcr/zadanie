# Budowanie środowiska
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Tworzenie finalnego obrazu
FROM python:3.12-slim
LABEL maintainer="Yelyzaveta Zlydnieva"
WORKDIR /app
COPY app.py .
COPY templates/ templates/
COPY --from=builder /install /usr/local
ENV PORT=5000
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:5000 || exit 1
CMD ["python", "app.py"]