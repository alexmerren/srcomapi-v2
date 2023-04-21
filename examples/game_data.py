import srcomapiv2 as api

def main():
    gameId = "k6qg0xdg"
    game_data = api.get_game_data(gameId)
    print(game_data)

if __name__ == "__main__":
    main()
