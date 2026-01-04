from .player import Player


def set_player_name(order: str) -> str:
    while True:
        name = input(f"Please insert player's {order} name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def player_factory(order: str, initial_score: int) -> Player:
    name = set_player_name(order)
    return Player(name=name, score=initial_score)


def initialize_players(n_players: int, initial_score: int) -> list[Player]:
    players: list[Player] = []

    arr = list("ABCD")
    sl = slice(0, n_players)

    for order in arr[sl]:
        player = player_factory(order, initial_score)
        players.append(player)

    return players
