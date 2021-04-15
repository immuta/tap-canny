"""Canny tap class."""

from pathlib import Path
from typing import List

from singer_sdk import Tap, Stream
from singer_sdk.typing import (
    DateTimeType,
    IntegerType,
    PropertiesList,
    Property,
    StringType,
)

from tap_canny.streams import (
    BoardsStream,
    PostsStream,
    StatusChangesStream,
    TagsStream,
    CommentsStream,
    VotesStream,
    ChangelogEntriesStream
)

STREAM_TYPES = [
    BoardsStream,
    PostsStream,
    StatusChangesStream,
    TagsStream,
    CommentsStream,
    VotesStream,
    ChangelogEntriesStream
]


class TapCanny(Tap):
    """Canny tap class."""

    name = "tap-canny"

    config_jsonschema = PropertiesList(
        Property("api_key", StringType, required=True),
        Property("limit", IntegerType),
        Property("start_date", DateTimeType),
    ).to_dict()


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""

        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# CLI Execution:

cli = TapCanny.cli
