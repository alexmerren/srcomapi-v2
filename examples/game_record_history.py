import srcomapiv2 as api

def main():
    gameId = "k6qg0xdg"
    game_data = api.get_game_data(gameId)
    categories = [category['id'] for category in game_data['categories']]
    categoryId = categories[0]
    record_history = api.get_game_category_record_history(gameId, categoryId)
    print(record_history)

if __name__ == "__main__":
    main()
