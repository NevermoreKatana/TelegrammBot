# TelegrammBot C.ai

![Logo](https://www.mlyearning.org/wp-content/uploads/2023/05/Character.AI-Review.jpg)


## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
<a href="https://codeclimate.com/github/NevermoreKatana/TelegrammBot/maintainability"><img src="https://api.codeclimate.com/v1/badges/a18bbde6ceb83d476c9c/maintainability" /></a>


## Описание
Телеграмм-бот, аналогичный сервису character.ai, предназначен для обработки запросов пользователя и взаимодействия с искусственным интеллектом с помощью заранее подготовленных инструкций, которые указывают, как именно AI должен действовать. Он предназначен для общения с предварительно созданными вымышленными или придуманными персонажами, чтобы поддерживать текстовую ролевую игру, помогать в творчестве или просто быть очень умным вымышленным другом!


## Базы данных
В данной системе используется единая база данных PostgreSQL.

Вся информация о пользователе - user_id, username, name и surname - хранится в таблице 'user_info'.

Информация о выбранном пользователем персонаже хранится в таблице 'characters'.

В таблице 'greetings' хранятся все предварительно подготовленные приветствия от персонажей.

Таблица 'prompts' содержит все инструкции (prompt'ы) для искусственного интеллекта, соответствующие каждому персонажу.

Таблица 'user_request' содержит все запросы от пользователя и ответы на эти запросы.

## Amplitude
В Amplitude отправляются события о регистрации, выборе персонажа, создании запроса от пользователя, получении запроса от искусственного интеллекта, а также отслеживании доставки сообщения до пользователя. Этот инструмент используется для сбора, анализа и визуализации данных о поведении пользователей в приложениях.

## Installation
Установка проекта
1. Создайте проект
2. Разверните виртуальное окружение
3. Установите библиотеки:
```bash
pip install -r requirements.txt
```
 4. Замените в openAi.py:
```
openai.api_key = TOKEN 
```
на свой OpenAi API TOKEN

 5. Замените в Main.py:
 ```
TOKEN = os.environ["TOKEN"]
URL = os.environ["URL"]
 ```
 На свой url для web-app и на свой TOKEN для telegram

 6. Замените в database/database_connection.py:
 ```
PG_USER = os.environ["PG_USER"]
PG_PASSWORD = os.environ["PG_PASSWORD"]
PG_DATABASE = os.environ["PG_DATABASE"]
PG_HOST = os.environ["PG_HOST"]
 ```
 На свои данные подключения к БД(PostgreSQL)

 7. Замените в telegramBot/Amplitude/send_event.py:
 ```
 api_key = os.environ["AMPL_API"]
 ```
 На свой ApiKey для Amplitude

8. Запуск Main.py

## Github HTTPS server
Для создания открытого https web-app использовался репозиторий на гитхабе настроенный как страница
- [@WEB-APP](https://github.com/NevermoreKatana/web-app)


## Optimizations

- Сохранение контекста(истории сообщений) и обнуление все истории когда меняется персонаж.
- Оптимизация обработки всех запросов к БД и Amplitude, чтобы пользователь быстрее получал сообщения
- Улучшение prompt'ов, чтобы пользователь не получал `грубых` или `некорректных` ответов


## Authors

- [@KatanaNevermore](https://github.com/NevermoreKatana)
- [@KatanaNevermore(Tg)](https://t.me/nevermorekatana)

## License

[MIT](https://github.com/NevermoreKatana/TelegrammBot/blob/main/LICENSE)

