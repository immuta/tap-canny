"""Stream class for tap-canny."""

import requests

from pathlib import Path
from typing import Any, Dict, Optional, Iterable
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
#Max amount of records that will be returned in an api call
RECORD_LIMIT = 99999

class CannyStream(RESTStream):
    """Canny stream class."""

    url_base = "https://canny.io/api/v1"
    rest_method = "POST"
    response_result_key = None

    def get_url_params(
        self,
        partition: Optional[dict],
        next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        return {"limit": RECORD_LIMIT}

    def prepare_request_payload(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Optional[dict]:
        return {"apiKey": self.config.get("api_key")}


    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()

        # if records are nested under a certain key, extract the records
        if self.response_result_key:
            resp_json = resp_json[self.response_result_key]

        if isinstance(resp_json, dict):
            yield resp_json
        else:
            for row in resp_json:
                yield row


class BoardsStream(CannyStream):
    """Boards stream class."""

    name = "boards"
    path = "/boards/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "boards"

    schema_filepath = SCHEMAS_DIR / "board.json"


class ChangelogEntriesStream(CannyStream):
    """Changelog Entries stream class."""

    name = "changelog_entries"
    path = "/entries/list"
    primary_keys = ["id"]
    replication_key = "lastSaved"
    response_result_key = "entries"

    schema_filepath = SCHEMAS_DIR / "changelog_entry.json"

class CommentsStream(CannyStream):
    """Comments stream class."""

    name = "comments"
    path = "/comments/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "comments"

    schema_filepath = SCHEMAS_DIR / "comment.json"


class PostsStream(CannyStream):
    """Posts stream class."""

    name = "posts"
    path = "/posts/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "posts"

    schema_filepath = SCHEMAS_DIR / "post.json"


class StatusChangesStream(CannyStream):
    """Status Changes stream class."""

    name = "status_changes"
    path = "/status_changes/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "statusChanges"

    schema_filepath = SCHEMAS_DIR / "status_change.json"


class TagsStream(CannyStream):
    """Tags stream class."""

    name = "tags"
    path = "/tags/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "tags"

    schema_filepath = SCHEMAS_DIR / "tag.json"


class VotesStream(CannyStream):
    """Votes stream class."""

    name = "votes"
    path = "/votes/list"
    primary_keys = ["id"]
    replication_key = "created"
    response_result_key = "votes"

    schema_filepath = SCHEMAS_DIR / "vote.json"
