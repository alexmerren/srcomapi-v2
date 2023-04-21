import srcomapiv2 as api
import json

def format_json(data):
    print(json.dumps(data, indent=4))

def main():
    game_id = "k6qg0xdg"
    game_data = api.get_game_data(game_id)
    categories = [category['id'] for category in game_data['categories']]
    category_id  = categories[0]
    data = api.get_game_category_record_history(game_id, category_id)
    format_json(data)

if __name__ == "__main__":
    main()
