import getopt
import sys

from elo_tool import config

HELP_RESPONSE = "hi! i will help you eventually. But sadly not currently."


def print_help():
    print(HELP_RESPONSE)


SHORT_OPTIONS = {
    "h": 0,
    "c": 1,

}

LONG_OPTIONS = {
    "help": 0,
    "config": 1,

}

OPTION_PROPERTIES = [
    [False, print_help],
    [True, config.load_config],

]


def parse_args():
    raw_args = sys.argv[1:]
    args = ([], [])
    try:
        args = getopt.gnu_getopt(raw_args,
                                 "".join([k + ":" if OPTION_PROPERTIES[SHORT_OPTIONS[k]][0] else k
                                          for k in SHORT_OPTIONS.keys()]),
                                 [k + "=" if OPTION_PROPERTIES[LONG_OPTIONS[k]][0] else k for k in LONG_OPTIONS.keys()])
    except getopt.GetoptError as e:
        print(e)
        print('\033[93m' + "The programm will execute without arguments" + '\033[0m')

    options, other = args

    if len(other) > 0:
        print('\033[93m' + f"{other} will be ignored" + '\033[0m')

    for option in options:
        name, arg = option
        num = SHORT_OPTIONS[name[1:]] if name[1:] in SHORT_OPTIONS else LONG_OPTIONS[name[2:]]
        option_properties = OPTION_PROPERTIES[num]
        if not option_properties[0]:
            arg = None

        print(f"option: {name}, arg: {arg}")

        if arg is None:
            option_properties[1]()
        else:
            option_properties[1](arg)
