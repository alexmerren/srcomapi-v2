import srcomapiv2 as api

def main():
    gameId = "k6qg0xdg"
    game_data = api.get_game_data(gameId)
    categories = [category['id'] for category in game_data['categories']]
    categoryId = categories[0]
    leaderboard_data = api.get_game_category_leaderboard(gameId, categoryId)
    print(leaderboard_data)

if __name__ == "__main__":
    main()

