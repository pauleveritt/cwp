from dataclasses import dataclass


@dataclass
class Guardian:
    """A parent or other adult for a player.

    Args:
        first_name: The guardian's first name.
        last_name: The guardian's last name.
    """
    first_name: str
    last_name: str
