# Science Platform

Научная платформа для публикации статей, управления пользовательскими аккаунтами и системы отзывов, разработанная на базе Django и Django REST Framework.

Проект реализует REST API и веб-интерфейс для работы с научными публикациями, а также включает систему аутентификации, тестирование API и контейнеризацию через Docker.

---

# Возможности проекта

- регистрация и авторизация пользователей;
- JWT / session authentication;
- создание и просмотр научных статей;
- система отзывов и рейтингов;
- поиск статей;
- REST API;
- fuzz-тестирование сериализаторов и API;
- Docker-конфигурация;
- HTML-шаблоны и frontend на JavaScript;
- middleware для обработки запросов.

---

# Технологии

## Backend

- Python 3.12
- Django
- Django REST Framework
- SQLite/PostgreSQL
- Pytest
- Hypothesis

## Frontend

- HTML5
- CSS3
- JavaScript

## DevOps

- Docker
- Docker Compose

---

# Структура проекта

```text
science_platform/
│
├── accounts/                # Приложение пользователей
│   ├── models.py            # Модель пользователя
│   ├── serializers.py       # DRF сериализаторы
│   ├── views.py             # API/views логика
│   ├── urls.py              # Роутинг приложения
│   ├── middleware.py        # Пользовательский middleware
│   └── migrations/          # Django миграции
│
├── article/                 # Приложение статей
│   ├── models.py            # Модели статей и отзывов
│   ├── serializers.py       # Сериализаторы статей/отзывов
│   ├── views.py             # API представления
│   ├── urls.py              # URL маршруты
│   ├── test/                # Fuzz-тестирование
│   │   ├── test_serializers_fuzz.py
│   │   └── test_views_fuzz.py
│   └── migrations/
│
├── science_platform/        # Основные настройки проекта
│   ├── settings.py          # Конфигурация Django
│   ├── urls.py              # Главные маршруты
│   ├── asgi.py              # ASGI entrypoint
│   └── wsgi.py              # WSGI entrypoint
│
├── templates/               # HTML шаблоны
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   └── register.html
│
├── static/                  # Статические файлы
│
├── Dockerfile               # Docker image
├── docker-compose.yml       # Docker orchestration
├── requirements.txt         # Python зависимости
├── pytest.ini               # Конфигурация pytest
└── manage.py                # Django management script
```

---

# Архитектура проекта

Проект разделён на два основных Django-приложения.

## accounts

Отвечает за:

- регистрацию пользователей;
- авторизацию;
- работу с пользовательской моделью;
- сериализацию данных аккаунтов;
- middleware для обработки запросов.

### Основные компоненты

| Файл | Назначение |
|---|---|
| `models.py` | модель пользователя |
| `serializers.py` | сериализация и валидация |
| `views.py` | API логика |
| `middleware.py` | middleware обработки запросов |
| `urls.py` | маршруты приложения |

---

## article

Отвечает за:

- создание научных статей;
- систему отзывов;
- поиск публикаций;
- REST API;
- тестирование.

### Основные компоненты

| Файл | Назначение |
|---|---|
| `models.py` | модели статей и отзывов |
| `serializers.py` | сериализация данных |
| `views.py` | CRUD/API логика |
| `urls.py` | маршруты API |
| `test/` | fuzz/property-based тестирование |

---

# Тестирование

В проекте реализовано fuzz/property-based тестирование с использованием Hypothesis.

Проверяются:

- сериализаторы;
- API endpoints;
- обработка случайных входных данных;
- устойчивость системы к некорректным запросам.

Запуск тестов:

```bash
pytest
```

---

# Запуск проекта

## Локальный запуск

### 1. Клонирование репозитория

```bash
git clone <repo_url>
cd science_platform
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Применение миграций

```bash
python manage.py migrate
```

### 5. Запуск сервера

```bash
python manage.py runserver
```

---

# Docker запуск

## Сборка и запуск контейнеров

```bash
docker-compose up --build
```

---

# API

## Основные endpoints

### Авторизация

| Метод | Endpoint | Описание |
|---|---|---|
| POST | `/register/` | регистрация |
| POST | `/login/` | вход |

---

### Статьи

| Метод | Endpoint | Описание |
|---|---|---|
| GET | `/articles/` | список статей |
| POST | `/articles/create/` | создание статьи |
| GET | `/articles/?search=` | поиск статей |

---

### Отзывы

| Метод | Endpoint | Описание |
|---|---|---|
| POST | `/reviews/create/` | создание отзыва |
| PUT | `/reviews/<id>/update/` | обновление отзыва |

---

# Frontend

Frontend реализован на HTML/CSS/JavaScript без использования SPA-фреймворков.

### Основные файлы

| Файл | Назначение |
|---|---|
| `home.js` | логика главной страницы |
| `auth.js` | авторизация |
| `api.js` | работа с API |
| `style.css` | общие стили |
| `home.css` | стили домашней страницы |

---

# Особенности проекта

- модульная архитектура;
- разделение backend/frontend;
- REST API;
- fuzz testing;
- Docker-ready инфраструктура;
- поддержка масштабирования;
- готовность к интеграции PostgreSQL;
- поддержка ASGI/WSGI.

---

# Автор

Проект разработан в рамках курсовой работы по дисциплине веб-разработки и проектирования информационных систем.

