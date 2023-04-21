import requests
import time
from srcomapiv2 import utils

__all__ = [
    "request_function_with_data",
    "request_function",
    "GAME_LIST",
    "GAME_DATA",
    "GAME_SUMMARY",
    "GAME_LEADERBOARD",
    "GAME_RECORD_HISTORY",
    "USER_DATA",
]

API_URL = "https://www.speedrun.com/api/v2/"
REQUEST_TIMEOUT_SLEEP = 2
REQUEST_TIMEOUT_CODES = [429, 503, 504]

GAME_LIST = "GameList"
GAME_DATA = "GameData"
GAME_SUMMARY = "GameSummary"
GAME_LEADERBOARD = "GameLeaderboard"
GAME_RECORD_HISTORY = "GameRecordHistory"
USER_DATA = "UserLeaderboard"

API_FUNCTIONS = {
    GAME_LIST: "GetGameList",
    GAME_DATA: "GetGameData",
    GAME_SUMMARY: "GetGameSummary",
    GAME_LEADERBOARD: "GetGameLeaderboard",
    GAME_RECORD_HISTORY: "GetGameRecordHistory",
    USER_DATA: "GetUserLeaderboard",
}

def request_get(url):
    response = requests.get(url)
    if response.status_code in REQUEST_TIMEOUT_CODES:
        print(f"{response.status_code}:{response.reason}")
        time.sleep(REQUEST_TIMEOUT_SLEEP)
        return request_get(url)
    return response

def request_function(function_name):
    url = create_api_url(function_name)
    return request_get(url).json()

def request_function_with_data(function_name, data):
    data['vary'] = utils.get_current_unix_time()
    header = utils.encode_b64_header(data)
    url = create_api_url(function_name, header=header)
    return request_get(url).json()

def create_api_url(function_name, header=None):
    if header is None:
        return f"{API_URL}{API_FUNCTIONS[function_name]}"
    return f"{API_URL}{API_FUNCTIONS[function_name]}?_r={header}"
