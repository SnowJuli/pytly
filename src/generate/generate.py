from PyInquirer import prompt
import requests
import yaml


def generateAccessToken(config):
    questions = [
        {
            'type': 'input',
            'name': 'username',
            'message': 'Email or Username of your account: ',
        },
        {
            'type': 'input',
            'name': 'password',
            'message': 'Password of your account: ',
        }
    ]
    options = prompt(questions)

    r = requests.post("https://api-ssl.bitly.com/oauth/access_token", auth=(options["username"], options["password"]))
    access_token = r.text
    try:
        print(f"Generated the following access token: '{access_token}' and saved it to the config file. Remember to keep this access token secret.")
        with open(config.config_path, "r") as f:
            contents = yaml.safe_load(f)
        with open(config.config_path, "w") as f:
            contents["access-token"] = access_token
            # Save the updated config
            yaml.dump(contents, f)
    except:
        print("Something went wrong")
        print(r)
        raise
