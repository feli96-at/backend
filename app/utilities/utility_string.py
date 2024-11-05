import random
import string

regex_object_id = "^[0-9a-f]{24}$"


def get_random_string(length: int, chars: str = string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(length))
