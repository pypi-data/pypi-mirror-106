from __future__ import annotations

import hashlib
from time import time
import asyncio
import json

from typing import TYPE_CHECKING
from . import errors

if TYPE_CHECKING:
    from .client import Client


TV_TOKEN_ENDPOINT = "http://tv.deezer.com/smarttv/8caf9315c1740316053348a24d25afc7/app_access_token.php?device=lg"
TV_AUTH_ENDPOINT = "http://tv.deezer.com/smarttv/8caf9315c1740316053348a24d25afc7/user_auth.php?&login={}&password={}&device=lg"


class Session:
    def __init__(self, client: Client) -> None:
        self.client = client
        self.logged_in = False
        self._token = ""
        self._expires = 0.0
        self.lock = asyncio.Lock()

    async def fetch_token(self):
        res = await self.client._req.get(TV_TOKEN_ENDPOINT)
        body = json.loads(await res.text())
        self._expires = time() + 3600  # 1 hour
        self._token = body["access_token"]

    async def token(self) -> str:
        async with self.lock:
            if self._expires < time():
                await self.fetch_token()
        return self._token

    async def login(self, email: str, password: str):
        pw = hashlib.md5(password.encode("utf-8")).hexdigest()
        url = TV_AUTH_ENDPOINT.format(email, pw)
        res = await self.client._req.get(url)
        body = json.loads(await res.text())
        if "error" in body:
            error = body["error"]
            raise errors.DeezerApiError(
                error["type"],
                error["message"],
                error["code"]
            )
        self._token = body["access_token"]
        self._expires = time() + 15780000  # 6 months
        self.logged_in = True

    async def logout(self):
        self.logged_in = False
        self._expires = 0
