from .swagger_client.configuration import Configuration

DEFAULT_HOST = ""


def set_default_host(new_host):
    global DEFAULT_HOST  # Use the global keyword to refer to the global variable
    DEFAULT_HOST = new_host


def get_default_config() -> Configuration:
    global DEFAULT_HOST
    ret = Configuration()
    ret.host = DEFAULT_HOST
    return ret
