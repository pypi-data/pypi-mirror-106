from typing import Literal, TypedDict

# https://trakt.docs.apiary.io/#introduction/required-headers
RequestHeaders = TypedDict(
    "RequestHeaders",
    {
        "authorization": str,
        "content-type": Literal["application/json"],
        "trakt-api-key": str,
        "trakt-api-version": Literal["2"],
    },
    total=False,
)
