from dotenv import load_dotenv
from system.myth import Myth
from os import environ

load_dotenv()
Myth(token=environ["TOKEN"])
