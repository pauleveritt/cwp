from dataclasses import dataclass, field
from typing import List, Iterable, Optional

from .guardian import Guardian


@dataclass
class Player:
    """A kid that plays in a lacrosse league.

    Players are the most important part of the league, obviously.
    But the player can't make it to practice without their folks.
    For this, we have the concept of a :py:class:`list of guardians <cwp.laxleague.guardian.Guardian>`.
    """
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)

    def add_guardians(self, guardians: Iterable[Guardian]):
        """Add one or more parents or adults to a player.

        Args:
            guardians: The adults to association with the player.

        """

        self.guardians.extend(guardians)

    @property
    def primary_guardian(self) -> Optional[Guardian]:
        return self.guardians[0] if self.guardians else None
