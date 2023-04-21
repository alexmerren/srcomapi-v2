import srcomapiv2 as api

def main():
    game_id = "k6qg0xdg"
    game_data = api.get_game_data(game_id)
    categories = [category['id'] for category in game_data['categories']]
    category_id = categories[0]
    leaderboard_data = api.get_game_category_leaderboard(game_id, category_id)
    print(leaderboard_data)

if __name__ == "__main__":
    main()
