import srcomapiv2 as api

def main():
    game_id = "k6qg0xdg"
    game_data = api.get_game_data(game_id)
    print(game_data)

if __name__ == "__main__":
    main()
