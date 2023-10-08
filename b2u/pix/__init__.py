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

