FROM gradle
WORKDIR /app
COPY . /app/
CMD ["gradle", "library system code.py"]