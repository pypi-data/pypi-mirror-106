from typing import Literal, TypedDict, Union
from hypeshed.common import iso_datetime
from .common import Episode, Show, Movie

class WatchingBase(TypedDict):
    started_at: iso_datetime
    expires_at: iso_datetime
    action: Literal["scrobble", "checkin"]

class WatchingEpisode(WatchingBase):
    type: Literal["episode"]
    show: Show
    episode: Episode

class WatchingMovie(WatchingBase):
    type: Literal["movie"]
    movie: Movie

# https://trakt.docs.apiary.io/#reference/users/watching/get-watching
Watching = Union[WatchingEpisode, WatchingMovie]
