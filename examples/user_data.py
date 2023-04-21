import srcomapiv2 as api

def main():
    user_id = "zxznzp0x"
    user_data = api.get_user_data(user_id)
    print(user_data)
    
if __name__ == "__main__":
    main()
