FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN "pip install -r requirements.txt"

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]