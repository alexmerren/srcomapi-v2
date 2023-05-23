import srcomapiv2 as api
from operator import itemgetter

def main():
    game_summary = api.get_game_summary('sm64')
    game_id = game_summary.get('game').get('id')
    game_data = api.get_game_data(game_id)
    leaderboard_combinations = sorted(game_data.get('runCounts'), key=itemgetter("count"), reverse=False)
    
    all_players = []
    for index, combination in enumerate(leaderboard_combinations):
        print(f"{index=},len={len(leaderboard_combinations)}")
        data = None
        if combination.get("ValueId") is None:
            data = api.get_game_category_leaderboard(combination.get("gameId"), combination.get("categoryId"))
        else:
            data = api.get_game_category_variable_value_leaderboard( \
                    combination.get("gameId"), \
                    combination.get("categoryId"), \
                    combination.get("variableId"), \
                    combination.get("valueId"))

        num_pages = getNumberOfPagesFromLeaderboard(data)

        for page in range(1, num_pages):
            if combination.get("ValueId") is None:
                data = api.get_game_category_leaderboard(combination.get("gameId"), combination.get("categoryId"), page_number=page)
            else:
                data = api.get_game_category_variable_value_leaderboard( \
                        combination.get("gameId"), \
                        combination.get("categoryId"), \
                        combination.get("variableId"), \
                        combination.get("valueId"), \
                        page_number=page)
            players = getPlayersFromLeaderboard(data)
            all_players.extend(players)

    with open('test.csv', 'w', encoding='utf-8') as openfile:
        openfile.write(','.join(all_players))

def getPlayersFromLeaderboard(data=None):
    if data is None:
        return []

    all_players = []

    players = data.get("leaderboard").get("players")
    for player in players:
        all_players.append(player.get("id"))        

    return all_players 

def getNumberOfPagesFromLeaderboard(data=None):
    if data is None:
        return 0 

    return data.get("leaderboard").get("pagination").get("pages")

if __name__ == "__main__":
    main()
