import srcomapiv2 as api

def main():
    game_id = "k6qg0xdg"
    game_data = api.get_game_data(game_id)
    game_url = game_data['game']['url']
    summary_data = api.get_game_summary(game_url)
    print(summary_data)
    
if __name__ == "__main__":
    main()
