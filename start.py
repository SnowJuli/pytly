from PyInquirer import prompt
import configargparse

from src.create.create import createBitlink
from src.expand.expand import expandBitlink
from src.information.information import getInformation


print("""Pytly - Made by Snowleoo
------------------------------------""")


def init_parser():
    parser = configargparse.ArgParser(
        config_file_parser_class=configargparse.YAMLConfigFileParser,
        default_config_files=["config.yaml"],
        description='CLI application for managing Bit.ly links'
    )
    parser.add_argument("-c", "--config-path", is_config_file=True, dest="config_path", help="path to the config file")
    parser.add_argument("-t", "--access-token", dest="access_token", help="Bit.ly access token")
    return parser.parse()


questions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'Which action do you want to perform?',
        "choices": [
            {
                'key': 's',
                'name': 'Shorten a Link',
                'value': "shorten"
            },
            {
                "key": "e",
                "name": "Expand a Bitlink",
                "value": "expand"
            },
            {
                "key": "i",
                "name": "Get information about a Bitlink",
                "value": "information"
            },
            {
                "key": "q",
                "name": "Quit",
                "value": "quit"
            }
        ],
    }
]


if __name__ == "__main__":
    config = init_parser()

    answers = prompt(questions)
    action = answers["action"]

    if action == "shorten":
        createBitlink(config)
    elif action == "expand":
        expandBitlink(config)
    elif action == "information":
        getInformation(config)
    elif action == "quit":
        pass
