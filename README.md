# Seattle Bot

This is a **Facebook Messenger Bot** implemented with FastAPI. It aims to provide a easy-to-use framework for developers to develop their own messenger chatBot.

---

## Main Services

Our bot provides the following **Content-Related** services:

* Real-time Seattle weather forecast
* Top 10 recommended restaurants of different categories (e.g., Japanese, Seafood)

This project also created **Python Wrapper** for [Facebook Messenger Platform](https://developers.facebook.com/docs/messenger-platform)
This wrapper has the following functions:

* `send_persistent_menu`
* `send_text_message`
* `send_quickreply_message`
* `send_template_message`
* `send_home_message`

## Prerequisites

Before running the app and utilizing our functions, you will need to do the following steps:

1. **Facebook**
    * Create a Facebook page and [Create a Facebook App](https://developers.facebook.com/apps/)
    * The default API version is v15.0
    * Obtain three things:
        * `PAGE_ACCESS_TOKEN` (get it from facebook development page)
        * `VERIFY_TOKEN` (determined by you, enter when connecting the page)
        * `META_APP_SECRET` (get it from facebook development page => Basic Info => Application Secret)

2. **Ngrok**
    * We use [Ngrok](https://ngrok.com/docs/getting-started) to expose our localhost server on the internet.
    * Please make sure to sign up and get your own `AUTH_TOKEN` to get full access of ngrok's function.

If you interested in our example chatBot

3. **Yelp**
    * Follow this [Blog](https://elfsight.com/blog/2020/11/how-to-get-and-use-yelp-api/) to get:
        * `YELP_CLIENT_ID`
        * `YELP_API_KEY`

## Installation

Clone this repository

```
git clone git@github.com:GaryHo34/SeattleBot.git
```

We provided two way to start the chatBot backend server

#### Start in local
Create your own venv environment and install all the dependencies

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Make your own .env file and fill the required env variable then

```
python3 main.py
```

After the FastAPI server is up, open a terminal and start a ngork service

```
ngrok http 8000
```

Verify your webhook url on the facebook developer dashboard.

#### Start in docker

Get your ngrok `AUTH_TOKEN` and paste it in `docker-compose.yml`
```
AUTH_TOKEN=<YOUR NGROK AUTH_TOKEN>
```

```
docker-compose up
```
You can find your ngrok url by visiting `localhost:4551`

Verify your webhook url on the facebook developer dashboard.


## Testing

To run test

```
python -m unittest -v tests/tests.py
```

## Repository Structure

```md
📦SeattleBot
 ┣ 📂example
 ┃ ┣ ┣ 📂api
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜weather.py
 ┃ ┃ ┗ 📜yelp.py
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜example.py
 ┃ ┣ 📂messenger
 ┃ ┣ 📜__init__.py
 ┃ ┗ 📜Messenger.py
 ┣ 📂model
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜DataModel.py
 ┃ ┗ 📜MessageModel.py
 ┣ 📜.env.sample
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜config.py
 ┣ 📜helper.py
 ┣ 📜main.py
 ┣ 📜requirements.txt
 ┗ 📜utils.py
```
