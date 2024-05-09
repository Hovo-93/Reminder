### Цель: Создание механизма напоминаний с использованием языковой модели.
### Стек:Python, Django, Aiogram, Asyncio, Celery, Redis,OpenAI Api

## Подготовка и запуск проекта
#### Шаг 1. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/Reminder.git
```
#### Шаг 2. Создайте в клонированной директории файл .env
```
Пример:

BOT_TOKEN=your_bot_key
MODEL=gpt-3.5-turbo
OPENAI_API_KEY= your_openai_api_key
```
#### Шаг 3.Создаем и применяем миграции:
```python
    python manage.py makemigrations
    python manage.py migrate

```
#### Шаг 4.Создаем  суперюзера для входа в Django Admin
```python
    python manage.py createsuperuser
```
#### Шаг 5. Выполняем команду
```python
    pip install -r requirements.txt
```
### Шаг 6. Запускаем бота 
```python
    python manage.py run_bot
```
### Шаг 7. Запуск celery worker
```bash
    celery -A reminder  worker --loglevel=info
```
### Шаг 8. Запуск celery beat
```bash
    celery --app reminder beat --loglevel=info
```