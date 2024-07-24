# Ваша Dockerfile
FROM python:3.9

# Встановити робочу директорію
WORKDIR /app

# Скопіювати всі файли в контейнер
COPY . /app

# Встановити залежності
RUN pip install -r requirements.txt

# Запустити вашу програму
CMD ["python", "app.py"]
