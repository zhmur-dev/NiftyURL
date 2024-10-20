# NiftyURL

---

## About

A simple and elegant Flask app that generates short URLs. Ready for deploy at any remote server.

Creates links that will look like ``https://<server_location>/<short_id>``, where `short_id` can be either specified by user, or generated automatically.

Can be used in two modes - minimalistic web interface and API.

---

## Stack

* Python 3.12
* Flask 2.0
* SQLAlchemy 1.4
* SQLite3

---

## Installation and startup

Clone the repo and change directory:

```
git clone https://github.com/zhmur-dev/NiftyURL.git
cd NiftyURL
```

Create and activate virtual environment:

```
# для Linux / MacOS:
python3 -m venv venv
source venv/bin/activate

# для Windows:
python -m venv venv
source venv/Scripts/activate
```

Update package manager and install requirements:

```
pip install --upgrade pip
pip install -r requirements.txt
```

Before launching the app for the first time, set the `FLASK_APP` variable in your virtual environment and update local database:

```
export FLASK_APP=niftyurl   # MacOS / Linux
set FLASK_APP=niftyurl      # Windows
flask db upgrade
```

Run the app:

```
flask run
```

For a standard local run, web interface is made available at: `http://127.0.0.1:5000/`.

For normal operation and server deploy please create an `.env` file in root directory and fill it based on the example provided in  `.env.example`.

---

### Operation in API mode

NifryURL processes API requests sent from any client.

To create a new short URL:
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

To obtain the original URL from database:
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

## Author
Alexander [zhmur-dev](https://github.com/zhmur-dev) Zhmurkov
