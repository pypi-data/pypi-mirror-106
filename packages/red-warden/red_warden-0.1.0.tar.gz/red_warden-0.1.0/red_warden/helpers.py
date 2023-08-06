import json
import datetime
import uuid
import socket
import random
import string
import secrets


def random_string(string_length=6, only_hex=False):
    if only_hex:
        """Generate a random string of hex"""
        return secrets.token_hex(int(string_length / 2))

    else:
        """Generate a random string of letters and digits"""
        letters_and_digits = string.ascii_letters + string.digits
        return "".join(random.choice(letters_and_digits) for i in range(string_length))


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        the_ip = s.getsockname()[0]
    except:
        the_ip = "127.0.0.1"
    finally:
        s.close()
    return the_ip


def get_random_element(elements, separator=","):
    if isinstance(elements, str):
        elements = elements.split(separator)

    return random.choice(elements)


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return obj.hex.upper()
        elif isinstance(obj, datetime.datetime):
            return datetime.datetime.strftime(obj, "%Y%m%d%H%M%S")
        elif isinstance(obj, datetime.date):
            return datetime.date.strftime(obj, "%Y%m%d")
        elif isinstance(obj, datetime.time):
            return datetime.time.strftime(obj, "%H%M%S")
        elif isinstance(obj, bytes):
            return obj.hex().upper()

        return super().default(obj)
