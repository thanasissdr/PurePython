from src.game.player import Player
from src.utils.parse_input import read_int


def player_play(player: Player) -> None:
    points = read_int(f"\nPlease insert {player.name}'s points (0-180): ")
    error = player.apply_turn(points)
    if error:
        print(error)
