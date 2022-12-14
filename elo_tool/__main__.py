# Todo:
#       cleanup parser
#       implement notion of current game(s)
#       add elo algorithm

import sys

from elo_tool import parser, config
import elo_tool.other.colors as COLOR
import elo_tool.other.data as DATA


def initialize():
    config.initialize()

    parser.parse_args()


def run():
    while True:
        input_string = input(">>")

        result = parser.parse_input(input_string)

        if result == -1:
            exit_program()


def exit_program():
    print("Are you sure you want to exit?")
    answer = ""
    while answer != "n" and answer != "no":
        answer = input("[y/n] ").lower()
        if answer == "y" or answer == "yes":
            print("\nexiting" + COLOR.DEFAULT)
            sys.exit()


def main():
    print('\033[2J')

    initialize()

    print(DATA.LOGO)

    try:
        run()
    except KeyboardInterrupt:
        exit_program()
