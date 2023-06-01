import srcomapiv2 as api
import json

def main():
    game_summary = api.get_game_summary('darksouls3')
    game_id = game_summary.get('game').get('id')
    game_data = api.get_game_data(game_id)
    categories = game_data.get('categories')
    for category in categories:
        category_id = category.get('id')
        history = api.get_game_category_record_history(game_id, category_id)
        print(json.dumps(history, indent=4))

if __name__ == "__main__":
    main()
