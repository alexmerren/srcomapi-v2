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

def get_user_data(userId, data=None):
    if data == None: 
        data = {
            "userId": userId,
            "levelType": 1,
        }
    return requests.request_function_with_data('UserLeaderboard', data)

def get_game_list(data=None):
    # The data here is useless, it maintains style with the other functions.
    return requests.request_function('GameList')

def get_game_data(gameId, data=None):
    if data == None: 
        data = {
            'gameId': gameId,
        }
    return requests.request_function_with_data('GameData', data)

def get_game_summary(gameUrl, data=None):
    if data == None: 
        data = {
            "gameUrl": gameUrl,
        }
    return requests.request_function_with_data('GameSummary', data)

def get_game_category_leaderboard(gameId, categoryId, data=None):
    if data == None:
        data = {
            "params": {
                "gameId": gameId,
                "categoryId": categoryId,
                "values": [],
                "timer":0,
                "regionIds":[],
                "platformIds":[],
                "video":0,
                "obsolete":0
            },
            "page":1,
        }
    return requests.request_function_with_data('GameLeaderboard', data)

def get_game_category_record_history(gameId, categoryId, data=None):
    if data == None:
        data = {
            "params": {
                "gameId": gameId,
                "categoryId": categoryId,
            },
        }
    return requests.request_function_with_data('GameRecordHistory', data)

def get_game_latest_leaderboard(gameId, limit, data=None):
    if data == None:
        data = {
            "gameId": gameId,
            "limit": limit
        }
    return requests.request_function_with_data('GameLatestLeaderboard', data)
