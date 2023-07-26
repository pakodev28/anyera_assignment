# PET API

## TECHNOLOGIES
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat&logo=Django%20REST%20Framework&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)
[![JWT](https://img.shields.io/badge/-JWT-464646?style=flat&color=043A6B)](https://jwt.io/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat&logo=NGINX&logoColor=ffffff&color=043A6B)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat&logo=gunicorn&logoColor=ffffff&color=043A6B)](https://gunicorn.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)
[![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat&logo=Docker&logoColor=ffffff&color=043A6B)](https://www.docker.com/)

## Linters and formatters
[![flake8](https://img.shields.io/badge/-flake8-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://flake8.pycqa.org/)
[![black](https://img.shields.io/badge/-black-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://github.com/psf/black)
[![isort](https://img.shields.io/badge/-isort-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://pycqa.github.io/isort/)

## Description

Проект "Pet API" - это REST API, разработанное для управления информацией о домашних животных. Приложение предоставляет возможность пользователям регистрироваться, аутентифицироваться и выполнять различные операции с информацией о своих питомцах. Пользователи могут добавлять, просматривать, обновлять и удалять данные о своих домашних животных.

### Основные функции проекта "Pet API" включают:
1) Регистрация и аутентификация пользователей: Пользователи могут зарегистрироваться в приложении, создав учетную запись с помощью username и password. После регистрации они могут войти в систему, указав свои учетные данные.

2) Управление информацией о питомцах: Пользователи могут добавлять информацию о своих домашних животных, такую как имя, возраст, порода и фотографию. Они также могут просматривать, обновлять и удалять данные о своих питомцах.

3) Фильтрация данных о питомцах: Пользователи могут фильтровать информацию о питомцахпо виду.

4) Аутентификация и авторизация: Доступ к операциям с данными о питомцах ограничен только зарегистрированным и аутентифицированным пользователям. Каждый пользователь может менять данные только о свих питомцах.


## Как развернуть проект:
1. Склонировать проект, перейти в папку config, настроить .env файл:
    ```
    git clone git@github.com:pakodev28/anyera_assignment.git
    ```
    ```
    cd anyera_assignment/config/
    ```
    ```
    copy .env.example .env
    ```
    ```
    cd ..
    ```
2. для запуска контейнеров:
    ```
    docker-compose up -d
    ```
3. Далее выполните следующие команды:
    ```
    docker-compose exec web python manage.py migrate --noinput
    ```
    ```
    docker-compose exec web python manage.py collectstatic --no-input
    ```
4. Можете загрузить тестовые данные в БД:
    ```
    docker-compose exec web python manage.py generate_test_data
    ```
5. Создайте суперпользователя если хотите использовать админку:
    ```
    docker-compose exec web python manage.py createsuperuser
    ```


### API EndPoints

Описание доступных эндроинтов находится в файле api_spec.yml (swagger-спецификация). Можно отрендерить через [онлайн редактор](https://editor.swagger.io/)(скопировать туда файл) или через соответствующий плагин для PyCharm или VSCode
