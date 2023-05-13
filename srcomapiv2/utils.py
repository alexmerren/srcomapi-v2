import json
import time
import base64

__all__ = [
    "get_current_unix_time",
    "encode_b64_header",
]

def get_current_unix_time():
    return int(time.time())

def decode_b64_header(header):
    padded = header + '='*divmod(len(header),4)[1]
    json_data = base64.urlsafe_b64decode(padded)
    data = json.loads(json_data)

    return data

def encode_b64_header(data):
    header_data_bytes = json.dumps(data).encode('utf-8')
    encoded_json = base64.urlsafe_b64encode(header_data_bytes)

    return encoded_json.decode('utf-8').replace("=", "", -1)
