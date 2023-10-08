import hmac
import hashlib
from base64 import b64encode

def hmac_hashing(api_secret, api_key, headers):
    try:
        nonce = headers["nonce"]
    except KeyError:
        raise ValueError("Headers do not contain 'nonce'")

    message = bytes(str(nonce) + api_key, 'utf-8')
    secret = bytes(api_secret, 'utf-8')

    signature = b64encode(
        hmac.new(secret, message, digestmod=hashlib.sha256).digest()
    )

    return signature

