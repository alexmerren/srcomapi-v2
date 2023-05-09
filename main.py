import srcomapiv2 as api
import json

def format_json(data):
    print(json.dumps(data, indent=4))

def main():
    game_summary = api.get_game_summary('smo')
    id = game_summary.get('game').get('id')
    game_data = api.get_game_data(id)
    format_json(game_data)

if __name__ == "__main__":
    main()
