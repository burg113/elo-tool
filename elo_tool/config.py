import os.path

import toml

DEFAULT_ELO = 800
DEFAULT_GAME_NAME = "Game"
DEFAULT_Players = []

game_name = DEFAULT_GAME_NAME
default_elo = DEFAULT_ELO
players = DEFAULT_Players
player_elo = {}


def set_game_name(name):
    global game_name
    game_name = name


def set_default_elo(def_elo):
    global default_elo
    default_elo = def_elo


def set_players(player_list):
    global players, player_elo, default_elo
    players = []
    player_elo = {}

    for player in player_list:

        if player in players:
            raise ValueError(f"player: {player} already in player list: {players}")

        players.append(player)


def set_elo(elo_dict):
    global player_elo, players
    player_elo = elo_dict

    for player in players:
        if player not in player_elo:
            player_elo[player] = default_elo


args = {
    "default_elo": (set_default_elo, DEFAULT_ELO),
    "name": (set_game_name, DEFAULT_GAME_NAME),
    "players": (set_players, DEFAULT_Players),
    "elo": (set_elo, default_elo),
}


def initialize():
    apply_config({})


def apply_config(config):
    for arg, value in args.items():
        fnc, default = value
        fnc(config[arg] if arg in config else default)


def load_config(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No config file at {path}")

    with open(path, "r") as config_file:
        print("_" * 100)
        print(config_file.read())
        print("_" * 100)

        config = toml.load(path)
        print(config)
        print("_" * 100)

        apply_config(config)

        game = game_state()
        pass


def game_state():
    global game_name, players, player_elo, default_elo

    return {"game_name": game_name,
            "players": players,
            "player_elo": player_elo,
            "default_elo": default_elo}
