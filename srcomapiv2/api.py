from srcomapiv2 import requests

__all__ = [
    "get_game_data",
    "get_game_summary",
    "get_user_data",
    "get_game_category_leaderboard",
    "get_game_latest_leaderboard",
    "get_game_category_record_history",
    "get_game_list",
]

def get_user_data(user_id, data=None):
    if data == None: 
        data = {
            "userId": user_id,
            "levelType": 1,
        }
    return requests.request_function_with_data('UserLeaderboard', data)

def get_game_list(data=None):
    # The data here is useless, it maintains style with the other functions.
    return requests.request_function('GameList')

def get_game_data(game_id, data=None):
    if data == None: 
        data = {
            'gameId': game_id,
        }
    return requests.request_function_with_data('GameData', data)

def get_game_summary(game_url, data=None):
    if data == None: 
        data = {
            "gameUrl": game_url,
        }
    return requests.request_function_with_data('GameSummary', data)

def get_game_category_leaderboard(game_id, category_id, page_number=1, data=None):
    if data == None:
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
    return requests.request_function_with_data('GameLeaderboard', data)

def get_game_category_record_history(game_id, category_id, data=None):
    if data == None:
        data = {
            "params": {
                "gameId": game_id,
                "categoryId": category_id,
            },
        }
    return requests.request_function_with_data('GameRecordHistory', data)

def get_game_latest_leaderboard(game_id, limit, data=None):
    if data == None:
        data = {
            "gameId": game_id,
            "limit": limit
        }
    return requests.request_function_with_data('GameLatestLeaderboard', data)
