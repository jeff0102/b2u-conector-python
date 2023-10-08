from b2u.lib.utils import check_required_parameter
from b2u.lib.utils import check_required_parameters

def get_ballance(self):
    """Get the ballance of the account

    GET /api/v1/b2ubank/balance/get-balance

    """
    return self.sign_request_with_body(
        "GET", "/api/v1/b2ubank/balance/get-balance"
    )


