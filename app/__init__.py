from datetime import time
from fastapi import FastAPI
from loguru import logger

app = FastAPI()

logger.add('debug{time}.log',  format='{time} :{level} : {message}', level='DEBUG', rotation='5 mb')

from  . import routes


