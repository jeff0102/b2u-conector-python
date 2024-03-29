from b2u.api import API


class B2u(API):
    def __init__(self, api_key=None, api_secret=None, **kwargs):
        if "base_url" not in kwargs:
            kwargs["base_url"] = "https://back.b2ubank.com"
        super().__init__(api_key, api_secret, **kwargs)

    # account info
    from b2u.pix._pix import get_ballance

    # pix key
    from b2u.pix._pix import get_pix_key_info
    from b2u.pix._pix import get_copypaste_pix_key_info
    from b2u.pix._pix import get_pix_keys_list # empty response from the server
    from b2u.pix._pix import delete_pix_key

    # transactions
    from b2u.pix._pix import get_transaction_info
    from b2u.pix._pix import get_statement
    from b2u.pix._pix import pix_withdrawal
    from b2u.pix._pix import pix_withdrawal_copypaste

    # webhook
    from b2u.pix._pix import deliver_webhook_urls

