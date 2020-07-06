from PyInquirer import prompt
import requests

def expandBitlink(config):
    questions = [
        {
            'type': 'input',
            'name': 'bitlink_id',
            'message': 'ID of the Link you want to expand: ',
        }
    ]
    options = prompt(questions)
    headers = {
        "Authorization": "Bearer " + config.access_token,
    }
    json = {
        "bitlink_id": options["bitlink_id"],
    }
    r = requests.post("https://api-ssl.bitly.com/v4/expand", headers=headers, json=json).json()
    try:
        print(f"Long Url: '{r['long_url']}'\n created at: '{r['created_at']}'\n with the ID '{r['id']}'")
    except KeyError:
        print("Something went wrong")
        print(r)
