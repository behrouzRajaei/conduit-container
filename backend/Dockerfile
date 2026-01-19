# ---------- Build Stage ----------
FROM python:3.7-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc g++ musl-dev postgresql-dev libffi-dev

COPY requirements.txt .
RUN pip install --user --upgrade pip && pip install --user -r requirements.txt

COPY . .

# ---------- Final Stage ----------
FROM python:3.7-alpine

WORKDIR /app

RUN apk add --no-cache postgresql-client

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY --from=builder /app /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["sh", "/app/entrypoint.sh"]
