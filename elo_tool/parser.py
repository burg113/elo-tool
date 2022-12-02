import getopt
import sys
import elo_tool.other.colors as color

from elo_tool import config

HELP_RESPONSE = "hi! i will help you eventually. But sadly not currently."


def print_help():
    print(HELP_RESPONSE)


ARGS_SHORT = {
    "h": 0,
    "c": 1,

}

ARGS_LONG = {
    "help": 0,
    "config": 1,
    "loadconfig": 1,

}

COMMANDS = {
    "h": 0,
    "help": 0,
    "config": 1,
    "loadconfig": 1

}

OPTION_PROPERTIES = [
    ["help", False, print_help],
    ["load config", True, config.load_config],
    ["save config", True, config.save_config]
]


def parse_args():
    raw_args = sys.argv[1:]
    args = ([], [])
    try:
        args = getopt.gnu_getopt(raw_args,
                                 "".join([k + ":" if OPTION_PROPERTIES[ARGS_SHORT[k]][1] else k
                                          for k in ARGS_SHORT.keys()]),
                                 [k + "=" if OPTION_PROPERTIES[ARGS_LONG[k]][1] else k for k in ARGS_LONG.keys()])
    except getopt.GetoptError as e:
        print(e)
        print(color.WARNING + "The programm will execute without arguments" + color.DEFAULT)

    options, other = args

    if len(other) > 0:
        print(color.WARNING + f"{other} will be ignored" + color.DEFAULT)

    print(color.ALT_COLOR + "Executing with:")
    for option in options:
        name, arg = option
        num = ARGS_SHORT[name[1:]] if name[1:] in ARGS_SHORT else ARGS_LONG[name[2:]]
        option_properties = OPTION_PROPERTIES[num]
        if not option_properties[1]:
            arg = None
            print(f"{option_properties[0]}, ignoring argument: {arg} as {option_properties[0]} requires no argument")
        else:
            print(f"{option_properties[0]} {arg}")

        if arg is None:
            option_properties[2]()
        else:
            option_properties[2](arg)
    print(color.DEFAULT, end="")


def parse_input(input_string):
    command, arg = None, None
    if " " in input_string:
        command, arg = input_string.split(" ", 1)
        command = command.strip()
        arg = arg.strip()

    else:
        command = input_string.strip()

    print(command, "#", arg)
    if command not in COMMANDS:
        print(f"'{command}' no such command exists")
        return False

    command_id = COMMANDS[command]
    if OPTION_PROPERTIES[command_id][1]:
        OPTION_PROPERTIES[command_id][2](arg)
    else:
        OPTION_PROPERTIES[command_id][2]()

    return True

