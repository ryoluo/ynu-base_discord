# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APP_ENV = os.environ.get("APP_ENV")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
