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
    "lang": "pt_BR" (Required)
    }

    """

    check_required_parameters([[recent_date, "recent_date"], [lastet_date, "lastet_date"]])
    body = {"from": recent_date, "to": lastet_date}

    return self.sign_request_with_body(
        "POST", "/api/v1/withdrawn/extract/transfers-b2ubank", body=body
    )
