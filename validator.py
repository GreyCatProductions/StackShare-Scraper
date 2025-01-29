import validators

def valid_url(url: str):
    return validators.url(url)