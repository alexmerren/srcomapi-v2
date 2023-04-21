import requests
from srcomapiv2 import utils

__all__ = [
    "request_function_with_data",
    "request_function",
]

API_URL = "https://www.speedrun.com/api/v2/"

API_REQUEST_QUERY = "?_r="

API_FUNCTIONS = {
    "GameList": "GetGameList",
    "GameData": "GetGameData",
    "GameSummary": "GetGameSummary",
    "GameLeaderboard": "GetGameLeaderboard",
    "GameLatestLeaderboard": "GetLatestLeaderboard",
    "GameRecordHistory": "GetGameRecordHistory",
    "UserLeaderboard": "GetUserLeaderboard",
}

# Example request headers found from the website. 
API_EXAMPLE_REQUEST_HEADER = {
    "GameList": "",
    "GameRecordHistory": "",
    "GameData": "eyJnYW1lSWQiOiI3NnI1NXZkOCIsInZhcnkiOjE2ODIwNzg0Mjd9",
    "GameSummary": "eyJnYW1lVXJsIjoic21vIiwidmFyeSI6MTY4MjA3ODQyN30",
    "GameLeaderboard": "eyJwYXJhbXMiOnsiZ2FtZUlkIjoiNzZyNTV2ZDgiLCJjYXRlZ29yeUlkIjoidzIwdzFsemQiLCJ2YWx1ZXMiOlt7InZhcmlhYmxlSWQiOiI2OGttM3c0bCIsInZhbHVlSWRzIjpbInpxb3l6MDIxIl19XSwidGltZXIiOjAsInJlZ2lvbklkcyI6W10sInBsYXRmb3JtSWRzIjpbXSwidmlkZW8iOjAsIm9ic29sZXRlIjowfSwicGFnZSI6MSwidmFyeSI6MTY4MjA4MzIyMX0",
    "GameLatestLeaderboard": "eyJnYW1lSWQiOiI3NnI1NXZkOCIsInZhcnkiOjE2ODIwNzg0MjcsImxpbWl0Ijo3fQ",
    "UserLeaderboard": "eyJ1c2VySWQiOiJ6eHpuenAweCIsImxldmVsVHlwZSI6MSwidmFyeSI6MTY1MjkwMDkyOH0",
}

def request_function(function_name):
    url = create_api_url(function_name)
    return requests.get(url).json()

def request_function_with_data(function_name, data):
    data['vary'] = utils.get_current_unix_time()
    header = utils.encode_b64_header(data)
    url = create_api_url(function_name, header=header)
    return requests.get(url).json()

def create_api_url(function_name, header=None):
    if header is None:
        return f"{API_URL}{API_FUNCTIONS[function_name]}"
    return f"{API_URL}{API_FUNCTIONS[function_name]}{API_REQUEST_QUERY}{header}"

