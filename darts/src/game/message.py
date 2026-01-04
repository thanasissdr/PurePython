from .player import Player


def score_message(player: Player) -> str:
    return f"Remaining points for {player.name}: {player.score}"


def winner_message(player_name: str) -> str:
    return f"{player_name} is the winner!!!"
