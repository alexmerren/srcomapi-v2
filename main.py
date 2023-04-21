import srcomapiv2 as api
import json

def format_json(data):
    print(json.dumps(data, indent=4))

def main():
    gameId = "k6qg0xdg"
    game_data = api.get_game_data(gameId)
    gameUrl = game_data['game']['url']
    game_summary_data = api.get_game_summary(gameUrl)
    format_json(game_summary_data)

if __name__ == "__main__":
    main()
