FROM python:3
WORKDIR /app
COPY . /app/
CMD ["python3", "library system code.py"]