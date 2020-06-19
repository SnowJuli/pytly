from src.create.create import createBitlink
from src.expand.expand import expandBitlink
from src.informations.informations import getInformations


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


if __name__ == "__main__":
    question()
