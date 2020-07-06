from PyInquirer import prompt

from src.create.create import createBitlink
from src.expand.expand import expandBitlink
from src.information.information import getInformation


def question():
    print("""Pytly - Made by Snowleoo
------------------------------------
1. Shorten a Link
2. Expand a Bitlink
3. Get informations of a Bitlink
4. Exit the Script""")

    option = input("Enter a number: ")

    if option == "1":
        createBitlink()

    if option == "2":
        expandBitlink()

    if option == "3":
        getInformations()

    if option == "4" or "exit":
        pass


print("""Pytly - Made by Snowleoo
------------------------------------""")

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
    answers = prompt(questions)
    action = answers["action"]

    if action == "shorten":
        createBitlink()
    elif action == "expand":
        expandBitlink()
    elif action == "information":
        getInformation()
    elif action == "quit":
        pass
