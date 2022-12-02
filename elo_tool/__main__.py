import sys

from elo_tool import parser, config
import elo_tool.other.colors as COLOR
import elo_tool.other.data as DATA


def initialize():

    config.initialize()

    parser.parse_args()

def run():
    input_string = input(">>")

    parser.parse_input(input_string)

def exit_program():
    print("\nexiting" + COLOR.DEFAULT)
    sys.exit()


def main():

    initialize()

    print('\033[2J')

    print(DATA.LOGO)

    try:
        run()
    except KeyboardInterrupt:
        exit_program()

