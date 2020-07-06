from PyInquirer import prompt
import requests


def createBitlink(config):
    questions = [
        {
            'type': 'input',
            'name': 'long_url',
            'message': 'URL you want to shorten: ',
        },
        {
            'type': 'input',
            'name': 'domain',
            'message': 'Domain to use for the shortened URL: ',
            "default": "bit.ly",
        },
        {
            'type': 'input',
            'name': 'group_guid',
            'message': 'Bit.ly group GUID (default=None): ',
        },
    ]
    options = prompt(questions)
    headers = {
        "Authorization": "Bearer " + config.access_token,
    }
    json = {
        "group_guid": options["group_guid"],
        "domain": options["domain"],
        "long_url": options["long_url"]
    }
    r = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers, json=json).json()
    try:
        print(f"Created the Bitlink '{r['link']}' pointing to '{r['long_url']}' and the ID '{r['id']}'")
    except KeyError:
        print("Something went wrong")
        print(r)
