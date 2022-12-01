from elo_tool import parser, config


def main():

    config.initialize()
    game = config.game_state()

    parser.parse_args()





