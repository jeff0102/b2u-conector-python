import json
from json import JSONDecodeError
import logging
import requests
from .__version__ import __version__
from b2u.error import ClientError, ServerError
from b2u.lib.utils import get_timestamp
from b2u.lib.utils import cleanNoneValue
from b2u.lib.authentication import hmac_hashing

class API(object):
    """API base class

    Keyword Args:
        base_url (str, optional): the API base url, useful to switch to testnet, etc. By default it's https://back.b2ubank.com
        timeout (int, optional): the time waiting for server response, number of seconds. https://docs.python-requests.org/en/master/user/advanced/#timeouts
        proxies (obj, optional): Dictionary mapping protocol to the URL of the proxy. e.g. {'https': 'http://1.2.3.4:8080'}
        show_limit_usage (bool, optional): whether return limit usage(requests and/or orders). By default, it's False
        show_header (bool, optional): whether return the whole response header. By default, it's False

    """

    def __init__(
        self,
        api_key=None,
        api_secret=None,
        base_url=None,
        timeout=None,
        proxies=None,
        show_limit_usage=False,
        show_header=False,
        private_key=None,
        private_key_pass=None,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.timeout = timeout
        self.proxies = None
        self.show_limit_usage = False
        self.show_header = False
        self.private_key = private_key
        self.private_key_pass = private_key_pass
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "b2u-conector-python" + __version__,
                "key": api_key,

            }
        )


        if show_limit_usage is True:
            self.show_limit_usage = True

        if show_header is True:
            self.show_header = True

        if type(proxies) is dict:
            self.proxies = proxies

        self._logger = logging.getLogger(__name__)
        return



    def sign_request_with_body(self, http_method, url_path, headers=None, body=None):
        if headers is None:
            headers = {}
        if body is None:
            body = {}
        headers["nonce"] = str(get_timestamp())
        headers["signature"] = self._get_sign(headers)
        return self.send_request_with_body(http_method, url_path, headers, body)

    def send_request_with_body(self, http_method, url_path, headers=None, body=None):
        if headers is None:
            headers = {}
        if body is None:
            body = {}

        url = self.base_url + url_path
        self._logger.debug("url: " + url)
        params = cleanNoneValue(
            {
                "url": url,
                "timeout": self.timeout,
                "proxies": self.proxies,
            }
        )

        response = self._dispatch_request_with_body(http_method, url, body, headers)
        self._logger.debug("raw response from server:" + response.text)
        self._handle_exception(response)

        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if self.show_limit_usage:
            limit_usage = {}
            for key in response.headers.keys():
                key = key.lower()
                if (
                        key.startswith("x-mbx-used-weight")
                        or key.startswith("x-mbx-order-count")
                        or key.startswith("x-sapi-used")
                ):
                    limit_usage[key] = response.headers[key]
            result["limit_usage"] = limit_usage

        if self.show_header:
            result["header"] = response.headers

        if len(result) != 0:
            result["data"] = data
            return result

        return data


    def _get_sign(self, headers):
        return hmac_hashing(self.api_secret, self.api_key, headers)

    def _dispatch_request_with_body(self, http_method, url, body, headers):
        request_func = {
            "GET": self.session.get,
            "POST": self.session.post,
        }.get(http_method)

        return request_func(url, json=body, headers=headers)

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, None, response.headers
                )
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], err["msg"], response.headers, error_data
            )
        raise ServerError(status_code, response.text)