from srcomapiv2 import requests

__all__ = [
    "get_game_data",
    "get_game_summary",
    "get_user_data",
    "get_game_category_leaderboard",
    "get_game_category_variable_value_leaderboard",
    "get_game_category_record_history",
    "get_game_list",
]

def get_user_data(user_id="", data=None):
    if data is None:
        data = {
            "userId": user_id,
            "levelType": 1,
        }

    return requests.request_function_with_data(requests.USER_DATA, data)

def get_game_list(page_number=1, data=None):
    if data is None:
        data = {
            "page": page_number,
        }

    return requests.request_function_with_data(requests.GAME_LIST, data)

def get_game_data(game_id="", data=None):
    if data is None:
        data = {
            'gameId': game_id,
        }

    return requests.request_function_with_data(requests.GAME_DATA, data)

def get_game_summary(game_url="", data=None):
    if data is None:
        data = {
            "gameUrl": game_url,
        }

    return requests.request_function_with_data(requests.GAME_SUMMARY, data)

def get_game_category_leaderboard(game_id="", category_id="", page_number=1, data=None):
    if data is None:
        data = {
            "params": {
                "gameId": game_id,
                "categoryId": category_id,
                "values": [],
                "timer":0,
                "regionIds":[],
                "platformIds":[],
                "video":0,
                "obsolete":0
            },
            "page": page_number,
        }

    return requests.request_function_with_data(requests.GAME_LEADERBOARD, data)

def get_game_category_variable_value_leaderboard(game_id="", category_id="", variable_id="", value_id="", page_number=1, data=None):
    if data is None:
        data = {
            "params": {
                "gameId": game_id,
                "categoryId": category_id,
                "values": [{
                    "variableId": variable_id,
                     "valueIds": [value_id]
                }],
                "timer":0,
                "regionIds":[],
                "platformIds":[],
                "video":0,
                "obsolete":0
            },
            "page": page_number,
        }

    return requests.request_function_with_data(requests.GAME_LEADERBOARD, data)

def get_game_category_record_history(game_id="", category_id="", data=None):
    if data is None:
        data = {
            "params": {
                "gameId": game_id,
                "categoryId": category_id,
            },
        }

    return requests.request_function_with_data(requests.GAME_RECORD_HISTORY, data)
