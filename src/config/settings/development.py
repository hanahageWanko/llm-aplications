from .base_setting import *
from dotenv import load_dotenv
load_dotenv()
import os

DEBUG = True

ALLOWED_HOSTS = ['*']

OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')