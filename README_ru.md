# NiftyURL

---

## О сервисе

Простой и изящный сервис на Flask для укорачивания ссылок. Готов к развёртке на любом удалённом сервере.

Образует ссылки вида ``https://<адрес_сервера>/<короткое_имя>``, при этом короткое имя можно задать самостоятельно, либо сгенерировать автоматически.

Работает в двух режимах - минималистичный веб-интерфейс и API.

---

## Стек технологий

* Python 3.12
* Flask 2.0
* SQLAlchemy 1.4
* SQLite3

---

## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/zhmur-dev/NiftyURL.git
cd NiftyURL
```

Создать и активировать виртуальное окружение:

```
# для Linux / MacOS:
python3 -m venv venv
source venv/bin/activate

# для Windows:
python -m venv venv
source venv/Scripts/activate
```

Обновить пакетный менеджер и установить зависимости из файла requirements.txt:

```
pip install --upgrade pip
pip install -r requirements.txt
```

Перед первым запуском приложения задать переменную `FLASK_APP` в виртуальном окружении и обновить локальную базу данных:

```
export FLASK_APP=niftyurl   # MacOS / Linux
set FLASK_APP=niftyurl      # Windows
flask db upgrade
```

Запустить приложение:

```
flask run
```

При стандартном локальном запуске веб-интерфейс сервиса будет доступен по адресу: `http://127.0.0.1:5000/`.

Для полноценной работы и деплоя на сервер в корневой директории сервиса нужно создать и заполнить файл `.env` по образцу, приведённому в `.env.example`.

---

## Работа в режиме API

Сервис обрабатывает API-запросы, отправленные из любого клиента.

На создание новой короткой ссылки:
```
POST  /api/id/

{
  "url": "string",
  "custom_id": "string"
}
```
```
201 CREATED

{
  "url": "string",
  "short_link": "string"
}
```

На получение оригинальной ссылки из базы данных:
```
GET  /api/id/{short_id}/
```
```
200 SUCCESSFUL

{
  "url": "string"
}
```

---

## Автор
Александр [zhmur-dev](https://github.com/zhmur-dev) Жмурков
