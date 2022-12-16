# Seattle Bot

This is a **Facebook Messenger Bot** implemented with FastAPI. It aims to provide users with Seattle local information and build wrapper for Facebook messenger platform for ease of use.

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
    * Obtain three things:
        * `PAGE_ACCESS_TOKEN` (get it from facebook development page)
        * `VERIFY_TOKEN` (determined by you, enter when connecting the page)
        * `META_API_URL`
2. **Yelp**
    * Follow this [Blog](https://elfsight.com/blog/2020/11/how-to-get-and-use-yelp-api/) to get:
        * `YELP_CLIENT_ID`
        * `YELP_API_KEY`

## Installation

Clone this repository

```
git clone git@github.com:GaryHo34/SeattleBot.git
```

Create your own venv environment

```
python3 -m venv .venv
. .venv/bin/activate
```

Install all the dependencies

```
pip install -r requirements.txt
```

Run the app

```
uvicorn main:app --reload
```

## Repository Structure

📦SeattleBot
 ┣ 📂api
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜weather.py
 ┃ ┗ 📜yelp.py
 ┣ 📂model
 ┃ ┣ 📜DataModel.py
 ┃ ┣ 📜MessageModel.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.DS_Store
 ┣ 📜.env.sample
 ┣ 📜.gitignore
 ┣ 📜README.md
 ┣ 📜constant.py
 ┣ 📜helper.py
 ┣ 📜main.py
 ┣ 📜requirements.txt
 ┗ 📜service.py
