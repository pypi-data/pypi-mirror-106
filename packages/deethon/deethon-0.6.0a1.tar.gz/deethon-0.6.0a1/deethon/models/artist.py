from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ShortArtist:
    """
    The Artist class contains several information about an artist.

    Attributes:
        id (int): The Deezer id of the artist.
        name (str): The name of the artist.
    """
    id: int
    name: str

    @property
    def link(self):
        return f"http://www.deezer.com/artist/{self.id}"

    @staticmethod
    def from_dict(d: dict) -> ShortArtist:
        return ShortArtist(d["id"], d["name"])


@dataclass
class Contributor:
    id: str
    name: str
    role: str

    @property
    def link(self):
        return f"http://www.deezer.com/artist/{self.id}"

    @staticmethod
    def from_dict(d: dict) -> Contributor:
        return Contributor(
            id=d["id"],
            name=d["name"],
            role=d["role"]
        )
