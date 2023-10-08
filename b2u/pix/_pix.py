from b2u.lib.utils import check_required_parameter
from b2u.lib.utils import check_required_parameters

def get_ballance(self):
    """Get The Balance Of The Account

    GET /api/v1/b2ubank/balance/get-balance

    """
    return self.sign_request_with_body(
        "GET", "/api/v1/b2ubank/balance/get-balance"
    )

def get_pix_key_info(self, key: str):
    """Get PIX Key Info

    GET /api/v1/bankUser/pix-info/:key

    Args:
    key : "string" (Required)

    """

    check_required_parameter(key, "key")
    path_completion = {"key": key}
    url_path = "/api/v1/bankUser/pix-info/{key}".format(**path_completion)

    return self.sign_request_with_body(
        "GET", url_path
    )

def get_transaction_info(self, transaction_id: str):
    """Get Transaction Info

    GET /api/v1/withdrawn/transaction/:transaction_id

    Args:
    transaction_id : "string" (Required)

    """

    check_required_parameter(transaction_id, "transaction_id")
    path_completion = {"transaction_id": transaction_id}
    url_path = "/api/v1/withdrawn/transaction/{transaction_id}".format(**path_completion)

    return self.sign_request_with_body(
        "GET", url_path
    )

def get_statement(self, recent_date: str, lastet_date: str):
    """POST Get Statement

    POST /api/v1/withdrawn/extract/transfers-b2ubank

    body (dict): JSON body for the request

    body = {
    "from": "2023-01-01" (Required),
    "to": "2023-03-02" (Required),
    }

    """

    check_required_parameters([[recent_date, "recent_date"], [lastet_date, "lastet_date"]])
    body = {"from": recent_date, "to": lastet_date}

    return self.sign_request_with_body(
        "POST", "/api/v1/withdrawn/extract/transfers-b2ubank", body=body
    )

def get_copypaste_pix_key_info(self, copypaste_key: str):
    """POST Get EMV Data

    POST /api/v1/withdrawn/b2bank-qr-data

    body (dict): JSON body for the request

    body = {
    "EMV": "00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913Fulano de Tal6008BRASILIA62070503***63041D3D"
    }

    """

    check_required_parameter(copypaste_key, "copypaste_key")
    body = {"EMV": copypaste_key}

    return self.sign_request_with_body(
        "POST", "/api/v1/withdrawn/b2bank-qr-data", body=body
    )

def get_pix_keys_list(self):
    """GET List PIX Keys

    GET /api/v1/bankUser/api/list-keys

    """

    return self.sign_request_with_body(
        "GET", "/api/v1/bankUser/api/list-keys"
    )

def delete_pix_key(self, key: str):
    """Delete PIX Key

    DELETE /api/v1/bankUser/api/delete-key/:key

    Args:
    key : "string" (Required)

    """

    check_required_parameter(key, "key")
    path_completion = {"key": key}
    url_path = "/api/v1/bankUser/api/delete-key/{key}".format(**path_completion)
    return self.sign_request_with_body(
        "DELETE", url_path
    )

def deliver_webhook_urls(self, withdrawURL: str, depositURL: str):
    """POST Webhook

    POST /api/v1/webhook

    body (dict): JSON body for the request

    body = {
    "withdrawURL": "https://test.com" (Required),
    "depositURL": "https://test.com" (Required),
    }

    """

    check_required_parameters([[withdrawURL, "withdrawURL"], [depositURL, "depositURL"]])
    body = {"withdrawURL": withdrawURL, "depositURL": depositURL}

    return self.sign_request_with_body(
        "POST", "/api/v1/webhook", body=body
    )

def get_copypaste_pix_key_info(self, copypaste_key: str):
    """POST Get EMV Data

    POST /api/v1/withdrawn/b2bank-qr-data

    body (dict): JSON body for the request

    body = {
    "EMV": "00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913Fulano de Tal6008BRASILIA62070503***63041D3D"
    }

    """

    check_required_parameter(copypaste_key, "copypaste_key")
    body = {"EMV": copypaste_key}

    return self.sign_request_with_body(
        "POST", "/api/v1/withdrawn/b2bank-qr-data", body=body
    )

def pix_withdrawal(self, key: str, keyType: str, amount: float):
    """POST Pix Withdrawal

    POST /api/v1/withdrawn/b2bank

    body (dict): JSON body for the request

    body = {
    "key": "11773574612" (Required),
    "keyType": "cpf" (Required),
    "amount": 2.20 (Required),
    "description": "anything"
    }

    """

    check_required_parameters([[key, "key"], [keyType, "keyType"], [amount, "amount"]])
    amount = "{:.2f}".format(amount)
    body = {"key": key, "keyType": keyType, "amount": amount, "description": "ok"}

    return self.sign_request_with_body(
        "POST", "/api/v1/withdrawn/b2bank", body=body
    )