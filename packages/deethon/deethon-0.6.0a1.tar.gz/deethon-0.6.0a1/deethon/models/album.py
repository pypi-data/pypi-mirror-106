from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from .. import Client


@dataclass
class ShortAlbum:
    id: int
    md5_image: str
    release_date: Optional[datetime]
    title: str

    @staticmethod
    def from_dict(d: dict) -> ShortAlbum:
        release_date = datetime.strptime(
            d["release_date"], "%Y-%m-%d") if "release_date" in d else None
        return ShortAlbum(
            id=d["id"],
            md5_image=d["md5_image"],
            release_date=release_date,
            title=d["title"]
        )


from .genre import Genre  # noqa: E402
from .artist import ShortArtist  # noqa: E402
from .track import ShortTrack  # noqa: E402


@dataclass
class Album:
    """
    The Album class contains several information about an album.

    Attributes:
        artist: The main artist of the album.
        duration: The duration in seconds of the album.
        genres: A list of genres of the album.
        id: The Deezer ID of the album.
        label: The label of the album.
        link: The Deezer link of the album.
        nb_tracks: The total number of tracks in the album.
        record_type: The record type of the album.
        release_date: The release date of the album.
        title: The title of the album.
        tracks: A list that contains basic tracks data.
        upc: The Universal Product Code (UPC) of the album.

    """
    artist: ShortArtist
    duration: int
    genres: list[Genre]
    id: int
    label: str
    link: str
    md5_image: str
    nb_tracks: int
    record_type: str
    release_date: datetime
    title: str
    tracks: list[ShortTrack]
    upc: str
    _client: Client

    @staticmethod
    def from_dict(client: Client, d: dict) -> Album:
        return Album(
            artist=ShortArtist.from_dict(d["artist"]),
            duration=d["duration"],
            genres=[Genre.from_dict(x) for x in d["genres"]["data"]],
            id=d["id"],
            label=d["label"],
            link=d["link"],
            md5_image=d["md5_image"],
            record_type=d["record_type"],
            release_date=datetime.strptime(d["release_date"], "%Y-%m-%d"),
            title=d["title"],
            tracks=[ShortTrack.from_dict(x)
                    for x in d["tracks"]["data"]],
            nb_tracks=d["nb_tracks"],
            upc=d["upc"],
            _client=client
        )

    def get_cover_url(self, size: int = 250, quality: int = 80) -> str:
        """
        Get the URL of the album cover.

        Args:
            size: The size of the album cover in pixels (should not exceed 1200).
            quality: The quality of the album cover (should be between 0 and 100).
        """
        return f"http://cdn-images.dzcdn.net/images/cover/{self.md5_image}/{size}x{size}-000000-{quality}-0-0.jpg"

    async def download_cover(self, size: int = 250, quality: int = 80) -> bytes:
        """
        Downloads the album cover.

        Args:
            size: The size of the album cover in pixels (should not exceed 1200).
            quality: The quality of the album cover (should be between 0 and 100).
        """
        cover_url = self.get_cover_url(size, quality)
        response = await self._client._req.get(cover_url)
        return await response.read()


@dataclass
class SearchAlbum:
    artist: ShortArtist
    id: int
    md5_image: str
    title: str
    genre_id: int
    record_type: str
    link: str
    nb_tracks: int

    @staticmethod
    def from_dict(d: dict) -> SearchAlbum:
        return SearchAlbum(
            artist=ShortArtist(d["artist"]["id"], d["artist"]["name"]),
            id=d["id"],
            md5_image=d["md5_image"],
            genre_id=d["genre_id"],
            link=d["link"],
            title=d["title"],
            record_type=d["record_type"],
            nb_tracks=d["nb_tracks"]
        )
