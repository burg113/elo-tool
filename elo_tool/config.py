import os.path

import toml

DEFAULT_ELO = 800
DEFAULT_GAME_NAME = "Game"
DEFAULT_Players = []

game_name = DEFAULT_GAME_NAME
default_elo = DEFAULT_ELO
players = DEFAULT_Players
player_elo = {}


def load_config(path):
    if not os.path.isfile(str(path)):
        print(f"No config file at '{path}'")
        return

    content = {}
    with open(path, "r") as config_file:
        apply_config(toml.load(path))


def save_config(path: str):
    content = {"name": game_name,
               "default_elo": default_elo,
               "players": players,
               "elo": player_elo}

    with open(path, "w") as file:
        file.write(toml.dumps(content))


def initialize():
    apply_config({})


def apply_config(config):
    for arg, value in args.items():
        fnc, default = value
        fnc(config[arg] if arg in config else default)


def set_game_name(name):
    global game_name
    game_name = name


def set_default_elo(def_elo):
    global default_elo
    default_elo = def_elo


def set_players(player_list: list):
    global players, player_elo, default_elo
    players = []
    player_elo = {}

    add_players(player_list)


def add_player(player: str):
    global players
    if player in players:
        raise ValueError(f"player: {player} already in player list: {players}")

    players.append(player)


def add_players(player_list: list):
    for player in player_list:
        add_player(player)


def set_elo(elo_dict):
    global player_elo, players
    player_elo = elo_dict

    for player in players:
        if player not in player_elo:
            player_elo[player] = default_elo


def set_elo(player: str, elo: int):
    global player_elo, players

    if player not in players:
        raise ValueError(f"player: {player} is not in player list: {players}")

    player_elo[player] = elo


def reset_elo(player: str):
    set_elo(player, DEFAULT_ELO)


args = {
    "default_elo": (set_default_elo, DEFAULT_ELO),
    "name": (set_game_name, DEFAULT_GAME_NAME),
    "players": (set_players, DEFAULT_Players),
    "elo": (set_elo, default_elo),
}


def game_state():
    global game_name, players, player_elo, default_elo

    return {"game_name": game_name,
            "players": players,
            "player_elo": player_elo,
            "default_elo": default_elo}


def print_stats():
    print("STATS:")
    for player, elo in player_elo.items():
        print(f"{player}\t\t{elo}")


def print_players():
    for player in players:
        print(player, end=", ")
    print()
