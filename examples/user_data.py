import srcomapiv2 as api

def main():
    userId = "zxznzp0x"
    user_data = api.get_user_data(userId)
    print(user_data)
    
if __name__ == "__main__":
    main()
