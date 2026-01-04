import argparse

from src.game.message import score_message, winner_message
from src.game.play import player_play
from src.game.setup import initialize_players


def main(n_players: int, initial_score: int = 501) -> None:
    players = initialize_players(n_players, initial_score)
    print(f"\nInitializing game with target of {initial_score}\n")

    while True:
        for player in players:
            player_play(player)
            if player.has_won():
                print(winner_message(player.name))
                return
            print(score_message(player))


def n_players_type(value: str) -> int:
    n = int(value)
    if not 2 <= n <= 4:
        raise argparse.ArgumentTypeError("n_players must be between 2 and 4")
    return n


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("--n_players", default=2, type=n_players_type)
    parser.add_argument("--initial_score", default=501, type=int, choices=[301, 501])

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(n_players=args.n_players, initial_score=args.initial_score)
