# Todo: refactor

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


class Config:
    # content, header
    def __init__(self, path=None, content=None, header: str = ""):
        if content is None:
            content = {}
        self.content = content
        self.header = header
        if path is not None:
            self.load(path)

    def load(self, path):
        if not os.path.isfile(str(path)):
            print(f"No config file at '{path}'")
            return

        with open(path, "r") as config_file:
            self.content = toml.load(path)

    def write(self, path, flag="w"):
        with open(path, flag) as file:
            file.write(self.header + "\n" + toml.dumps(self.content))

    def __str__(self):
        return str(self.content)


def initialize():
    apply_config({})


def apply_config(config):
    for arg, value in args.items():
        fnc, default = value
        fnc(config[arg] if arg in config else default)


def load_config(path):
    config = Config(str(path))

    apply_config(config.content)


def generate_config() -> Config:
    config = Config(header="# this is a automatically generated config\n\n")
    config.content = {"name": game_name,
                      "default_elo": default_elo,
                      "players": players,
                      "elo": player_elo}

    return config


def save_config(path: str):
    generate_config().write(path)


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

def __str__(self):
    return "foo"
