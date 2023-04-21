import srcomapiv2 as api
import json

def format_json(data):
    print(json.dumps(data, indent=4))

def main():
    user_id = "zxznzp0x"
    data = api.get_user_data(user_id)
    format_json(data)

if __name__ == "__main__":
    main()
