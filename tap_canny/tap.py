"""Canny tap class."""

from pathlib import Path
from typing import List

from singer_sdk import Tap, Stream
from singer_sdk.typing import (
    ArrayType,
    BooleanType,
    DateTimeType,
    IntegerType,
    NumberType,
    ObjectType,
    PropertiesList,
    Property,
    StringType,
)

# TODO: Import your custom stream types here:
from tap_canny.streams import (
    CannyStream,
    BoardsStream,
    PostsStream,
    StatusChangesStream,
    TagsStream,
    CommentsStream,
    VotesStream,
    ChangelogEntriesStream
)


# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    BoardsStream
]


class TapCanny(Tap):
    """Canny tap class."""

    name = "tap-canny"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = PropertiesList(
        Property("api_key", StringType, required=True),
        Property("start_date", DateTimeType),
    ).to_dict()


    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


# CLI Execution:

cli = TapCanny.cli
