
# [project name]

![aiogram](https://img.shields.io/badge/python-v3.12.7-blue.svg?logo=python&logoColor=yellow) ![aiogram](https://img.shields.io/badge/aiogram-v3.15.0-blue.svg?logo=telegram) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

About ...

## Features

The bot provides the following features:

- ...
- ...

## Commands

The bot has several commands that can be used to access its features:

- `/start`: Sends a ...
- `/help`: Sends a ...

## Requirements

- Python v3.12.7
- aiogram v3.15.0
- dotenv v1.0.1

## Installation

To get started with this bot, follow these steps:

- Clone this repository

    ```
    $ git clone [source]
    $ cd [source]
    ```

- Create a new bot on Telegram by talking to the [BotFather](https://t.me/BotFather), and obtain the API token.

- Rename the file `.env.dist` to `.env` and replace the placeholders with required data.

- Create a virtual environment and install required dependencies.

    ```
    $ python -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements/local.txt
    ```

- Run the bot using `python -m bot`

- To run the bot with Docker `sudo docker compose up -d --build`
