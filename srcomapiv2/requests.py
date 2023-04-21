import requests
import time
from srcomapiv2 import utils

__all__ = [
    "request_function_with_data",
    "request_function",
]

API_URL = "https://www.speedrun.com/api/v2/"

API_REQUEST_QUERY = "?_r="

API_REQUEST_TIMEOUT_SLEEP = 2
API_REQUEST_TIMEOUT_CODES = [429, 503, 504]

API_FUNCTIONS = {
    "GameList": "GetGameList",
    "GameData": "GetGameData",
    "GameSummary": "GetGameSummary",
    "GameLeaderboard": "GetGameLeaderboard",
    "GameLatestLeaderboard": "GetLatestLeaderboard",
    "GameRecordHistory": "GetGameRecordHistory",
    "UserLeaderboard": "GetUserLeaderboard",
}

def request(url):
    response = requests.get(url)
    if response.status_code in API_REQUEST_TIMEOUT_CODES:
        print(f"{response.status_code}:{response.reason}")
        time.sleep(API_REQUEST_TIMEOUT_SLEEP)
        return request(url)
    return response

def request_function(function_name):
    url = create_api_url(function_name)
    return request(url).json()

def request_function_with_data(function_name, data):
    data['vary'] = utils.get_current_unix_time()
    header = utils.encode_b64_header(data)
    url = create_api_url(function_name, header=header)
    return request(url).json()

def create_api_url(function_name, header=None):
    if header is None:
        return f"{API_URL}{API_FUNCTIONS[function_name]}"
    return f"{API_URL}{API_FUNCTIONS[function_name]}{API_REQUEST_QUERY}{header}"
