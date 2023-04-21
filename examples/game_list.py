import srcomapiv2 as api

def main():
    game_list_data = api.get_game_list()
    print(game_list_data)

if __name__ == "__main__":
    main()
