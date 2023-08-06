"""
This module contains several constants.
"""

import re


PUBLIC_API_URL: str = "https://api.deezer.com/"
"""The url of Deezer's official API server."""

DEEZER_LINK_REGEX: re.Pattern = re.compile(
    r"https?://(?:www\.)?deezer\.com/(?:\w+/)?(\w+)/(\d+)")
