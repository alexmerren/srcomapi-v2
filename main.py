import srcomapiv2 as api

def main():
    game_summary = api.get_game_summary('sm64')
    game_id = game_summary['game']['id']
    game_data = api.get_game_data(game_id)
    print(game_data['game']['totalPlayerCount'])
    leaderboard_combinations = game_data['runCounts']
    all_players = set()
    with open('sm64.csv', 'w', encoding='utf-8') as openfile:
        for index, combination in enumerate(leaderboard_combinations):
            data = None
            if combination.get('ValueId') is None:
                data = api.get_game_category_leaderboard(combination['gameId'], combination['categoryId'])
            else:
                data = api.get_game_category_variable_value_leaderboard( \
                        combination['gameId'], \
                        combination['categoryId'], \
                        combination['variableId'], \
                        combination['valueId'])

            num_pages = data['leaderboard']['pagination']['pages']

            for page in range(0, num_pages+1):
                print(f'{index=},len={len(leaderboard_combinations)},{page=},len_pages={num_pages}')
                if combination.get('ValueId') is None:
                    data = api.get_game_category_leaderboard(combination['gameId'], combination['categoryId'], page_number=page)
                else:
                    data = api.get_game_category_variable_value_leaderboard( \
                            combination['gameId'], \
                            combination['categoryId'], \
                            combination['variableId'], \
                            combination['valueId'], \
                            page_number=page)

                players = data['leaderboard']['players']
                for player in players:
                    all_players.add(player['id'])

        openfile.write('\n'.join(all_players))
        print(len(all_players))

if __name__ == "__main__":
    main()
