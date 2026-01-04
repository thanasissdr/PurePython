from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int = 501

    def apply_turn(self, points: int) -> str | None:
        if points < 0:
            return "Points cannot be negative."

        elif points > 180:
            return "Invalid turn score. Must be between 0 and 180."

        elif points > self.score:
            return (
                f"Bust! {points} exceeds {self.name}'s remaining score: {self.score}."
            )

        self.score -= points
        return None

    def has_won(self) -> bool:
        return self.score == 0
