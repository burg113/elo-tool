import getopt
import sys
import elo_tool.other.colors as color

from elo_tool import config, __main__

HELP_RESPONSE = "hi! i will help you eventually. But sadly not currently. ¯\\_(ツ)_/¯ "

flag = 0
FLAGS = {
    "exit": -1
}


def print_help():
    print(HELP_RESPONSE)


def set_flag(val):
    global flag
    flag = val


ARGS_SHORT = {
    "h": 0,
    "c": 1,

}

ARGS_LONG = {
    "help": 0,
    "config": 10,
    "loadconfig": 10,

}

COMMANDS = {
    "h": 0,
    "help": 0,
    "exit": 1,
    "exit()": 1,
    "config": 10,
    "loadconfig": 10

}

OPTION_PROPERTIES = {
    0: ["help", False, print_help],
    1: ["exit", False, lambda: set_flag(-1)],

    10: ["load config", True, config.load_config],
    11: ["save config", True, config.save_config]
}


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
        print(color.WARNING + "The program will execute without arguments" + color.DEFAULT)

    options, other = args

    if len(other) > 0:
        print(color.WARNING + f"{other} will be ignored" + color.DEFAULT)

    print(color.ALT_COLOR + "Executing with:")
    for option in options:
        name, arg = option
        num = ARGS_SHORT[name[1:]] if name[1:] in ARGS_SHORT else ARGS_LONG[name[2:]]
        option_properties = OPTION_PROPERTIES[num]
        if not option_properties[1]:
            if arg is not None and arg != "":
                print(
                    f'{option_properties[0]}, ignoring argument: {arg} as {option_properties[0]} requires no argument')
            else:
                print(option_properties[0])
            arg = None
        else:
            print(f'{option_properties[0]} \t\t {arg}')

        if arg is None:
            option_properties[2]()
        else:
            option_properties[2](arg)
    print(color.DEFAULT, end="")


def parse_input(input_string):
    if len(input_string.strip()) == 0:
        return
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
        return 0

    command_id = COMMANDS[command]
    if OPTION_PROPERTIES[command_id][1]:
        OPTION_PROPERTIES[command_id][2](arg)
    else:
        OPTION_PROPERTIES[command_id][2]()

    if FLAGS["exit"] == flag:
        return -1
    return 1
