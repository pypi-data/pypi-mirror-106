from os import environ
from dotenv import load_dotenv
import requests
import json
import logging


class RedcapClient:
    load_dotenv()
    logger = logging.Logger

    def __str__(self):
        return 'RedcapClient'

    def __init__(self):
        self.logger = logging.Logger(self.__str__())

    def send_record(self, dict_answers: dict):
        fields = {
            'token': environ['API_TOKEN'],
            'content': 'record',
            'format': 'json',
            'type': 'flat',
            'data': json.dumps([dict_answers]),
        }
        r = requests.post(environ['API_URL'], data=fields)

        self.logger.info(f'[REDCAP RESPONSE]: HTTP Status: {r.status_code}')
        self.logger.info(f'[REDCAP RESPONSE BODY]: {r.text}')
        return r.status_code, r.text
