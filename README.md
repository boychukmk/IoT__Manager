# IoT Management

## Опис
Додаток для управління IoT пристроями з використанням PostgreSQL та Peewee ORM. Асинхронний API на базі aiohttp, працює в контейнерах Docker.

## Налаштування

1. **Створіть файл `.env` у кореневій директорії проєкту з наступним вмістом та задайте значення змінних:**
    ```env
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
    ```

2.  **Запустіть Docker контейнери:**
    ```bash
    docker-compose up --build
    ```

3.  **Перевірте лог контейнера `app` для підтвердження, що сервер API успішно запущено:**
    ```bash
    docker-compose logs -f app
    ```

4. **Запустіть скрипт для ініціалізації бази даних та заповнення її даними:**
    ```bash
    docker-compose exec app python populate_db.py
    ```
Certainly! You can use Markdown to create a gray background for the section by using blockquotes. Here is the updated README file with the requested formatting:

## ФУНКЦІОНАЛЬНІСТЬ API 

> ### POST /devices
> Додає нові пристрої у бд
> 
> **Запит:**
> - **URL:** `/devices`
> - **Метод:** POST
> - **Приклад запросу:** JSON
>     ```json
>     {
>       "name": "New Device",
>       "type": "TypeX",
>       "login": "newlogin",
>       "password": "newpass",
>       "location_id": 1,
>       "api_user_id": 1
>     }
>     ```
> 
> **Відповідь:**
> - **Статус:** 201 Created
> - **Приклад відповіді:** JSON
>     ```json
>     {
>       "id": 4
>     }
>     ```

> ### GET /devices/{id}
> Витягує пристрій за id
> 
> **Запит:**
> - **URL:** `/devices/{id}`
> - **Метод:** GET
> 
> **Відповідь:**
> - **Статус:** 200 OK
> - **Приклад відповіді:** JSON
>     ```json
>     {
>       "name": "Device Name",
>       "type": "Device Type",
>       "login": "device_login",
>       "password": "device_password",
>       "location_id": 1,
>       "api_user_id": 1
>     }
>     ```
> - **Статус:** 404 Not Found (якщо пристрій не знайдено)
> - **Приклад відповіді:** JSON
>     ```json
>     {
>       "error": "Device not found"
>     }
>     ```

> ### PUT /devices/{id}
> Оновлює інформацію про пристрій 
> 
> **Запит:**
> - **URL:** `/devices/{id}`
> - **Метод:** PUT
> - **Приклад запиту:** JSON
>     ```json
>     {
>       "name": "Updated Device",
>       "type": "UpdatedType",
>       "login": "updatedlogin",
>       "password": "updatedpass",
>       "location_id": 2,
>       "api_user_id": 2
>     }
>     ```
> 
> **Відповідь:**
> - **Статус:** 200 OK
> - **Приклад відповіді:**
>     ```text
>     Device updated
>     ```
> - **Статус:** 404 Not Found (якщо пристрій не існує)
> - **Приклад відповіді:** JSON
>     ```json
>     {
>       "error": "Device not found"
>     }
>     ```

> ### DELETE /devices/{id}
> Видаляє пристрій за id
> 
> **Запит:**
> - **URL:** `/devices/{id}`
> - **Метод:** DELETE
> 
> **Відповідь:**
> - **Статус:** 200 OK
> - **Приклад відповіді:**
>     ```text
>     Device deleted
>     ```
> - **Статус:** 404 Not Found (якщо пристрій не існує)
> - **Приклад відповіді:** JSON
>     ```json
>     {
>       "error": "Device not found"
>     }
>     ```


## Тестування за допомогою curl: ##
- ***Додавання пристрою у бд:***
```bash
docker-compose exec app curl -X POST http://localhost:8000/devices \
    -H "Content-Type: application/json" \
    -d '{
    "name": "New Device", 
    "type": "TypeX", 
    "login": "newlogin",
     "password": "newpass", 
     "location_id": 1, 
     "api_user_id": 1
     }'

```
- ***Пошук пристрою у бд:***
```bash
docker-compose exec app curl -X GET http://localhost:8000/devices/2
```
- ***Оновлення пристрою з бд:***
```bash
docker-compose exec app curl -X PUT http://localhost:8000/devices/2 \
    -H "Content-Type: application/json" \
    -d '{
    "name": "Updated Device", 
    "type": "UpdatedType", 
    "login": "updatedlogin", 
    "password": "updatedpass", 
    "location_id": 2, 
    "api_user_id": 2
    }'
```
- ***Видалення пристрою з бд:***
```bash
docker-compose exec app curl -X DELETE http://localhost:8000/devices/4
```
