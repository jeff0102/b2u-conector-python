#!/usr/bin/env python

import logging
from b2u.pix import B2u as Client
from b2u.lib.utils import config_logging
from b2u.error import ClientError
from examples.utils.prepare_env import get_api_key

config_logging(logging, logging.INFO)

api_key, api_secret = get_api_key()

client = Client(api_key, api_secret)

try:
    response = client.get_statement("2023-10-1", "2023-10-08")
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
