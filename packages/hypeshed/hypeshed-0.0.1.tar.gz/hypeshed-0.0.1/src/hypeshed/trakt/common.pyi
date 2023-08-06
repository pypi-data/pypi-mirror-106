from typing import TypedDict

class MediaIdsBase(TypedDict):
    trakt: int
    imdb: str
    tmdb: int

class ShowIds(MediaIdsBase):
    slug: str
    tvdb: int

class EpisodeIds(MediaIdsBase):
    tvdb: int

class MovieIds(MediaIdsBase):
    slug: str

class MediaBase(TypedDict):
    title: str

class Episode(MediaBase):
    season: int
    episode: int
    ids: EpisodeIds

class Show(MediaBase):
    year: int
    ids: ShowIds

class Movie(MediaBase):
    year: int
    ids: MovieIds
