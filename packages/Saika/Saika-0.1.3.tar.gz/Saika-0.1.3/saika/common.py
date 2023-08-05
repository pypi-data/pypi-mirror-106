import base64

from itsdangerous import TimedJSONWebSignatureSerializer

from .environ import Environ


def obj_encrypt(obj, expires_in=None):
    return TimedJSONWebSignatureSerializer(Environ.app.secret_key, expires_in).dumps(obj).decode()


def obj_decrypt(obj_str):
    try:
        return TimedJSONWebSignatureSerializer(Environ.app.secret_key).loads(obj_str)
    except:
        return None


def obj_standard(obj, str_key=False, str_obj=False):
    this = lambda x: obj_standard(x, str_key, str_obj)
    if type(obj) in [bool, int, float, str, type(None)]:
        return obj
    elif isinstance(obj, bytes):
        return base64.b64encode(obj).decode()
    elif isinstance(obj, list):
        return [this(i) for i in obj]
    elif isinstance(obj, dict):
        return {str(k) if str_key else this(k): this(v) for k, v in obj.items()}
    else:
        return str(obj) if str_obj else obj
