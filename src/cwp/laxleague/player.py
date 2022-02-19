from dataclasses import dataclass, field
from typing import List, Iterable, Optional

from .guardian import Guardian


@dataclass
class Player:
    first_name: str
    last_name: str
    guardians: List[Guardian] = field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)

    def add_guardians(self, guardians: Iterable[Guardian]):
        self.guardians.extend(guardians)

    @property
    def primary_guardian(self) -> Optional[Guardian]:
        return self.guardians[0]  # if self.guardians else None
