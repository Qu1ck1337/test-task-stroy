## Переменные окружения
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=product_db
DATABASE_URL=postgresql://postgres:password@db:5432/product_db
```

## Запуск приложения

#### Через терминал
```commandline
poetry run uvicorn app.main:app --reload
```

#### С использованием Docker
```commandline
docker-compose up --build
```


## Документация API
* Swagger UI: http://localhost:8000/docs
* oc: http://localhost:8000/redoc

## Эндпойнты

### Категории
* `POST /categories/` - Создание категории
* `GET /categories/` - Получение списка категорий
* `GET /categories/{category_id}` - Получение категории по ID

### Продукты
* `POST /products/` - Создание продукта
* `GET /products/` - Получение списка продуктов с фильтрацией
* `GET /products/{product_id}` - Получение продукта по ID
* `PUT /products/{product_id}` - Полное обновление продукта
* `PATCH /products/{product_id}` - Частичное обновление продукта
* `GET /products/{product_id}` - Удаление продукта

## Запуск тестов
```commandline
poetry run pytest
```