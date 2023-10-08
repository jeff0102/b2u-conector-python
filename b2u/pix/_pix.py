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

    GET api/v1/bankUser/pix-info/:key

    Args:
    key (str): El valor de la variable dinámica ":key" que se agregará al final de la URL.

    """

    check_required_parameter(key, "key")
    path_completion = {"key": key}
    url_path = "/api/v1/bankUser/pix-info/{key}".format(**path_completion)

    return self.sign_request_with_body(
        "GET", url_path
    )

