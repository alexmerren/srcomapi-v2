import srcomapiv2 as api
import json

def format_json(data):
    print(json.dumps(data, indent=4))

def main():
    data = api.get_game_list()
    num_pages = data['pagination']['pages']
    all_games = set()
    for page_number in range(1, num_pages):
        data = api.get_game_list(page_number)
        games = data['games']
        for game in games:
            all_games.add(game['id'])

    with open('test.csv', 'w', encoding='utf-8') as openfile:
        game_string = ','.join(list(all_games)) + '\n'
        openfile.write(f"Number of games: {len(all_games)}")
        openfile.write(game_string)

if __name__ == "__main__":
    main()
