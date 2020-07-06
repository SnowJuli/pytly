from PyInquirer import prompt
import requests


def createBitlink():
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
            'message': 'Bit.ly group GUID: ',
            "default": "",
        },
    ]
    options = prompt(questions)
    headers = {
        "group_guid": options["group_guid"],
        "domain": options["domain"],
        "long_url": options["long_url"]
    }
    r = requests.post("https://api-ssl.bitly.com/v4/shorten", headers=headers)
    print(r.text)
