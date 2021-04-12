"""Stream class for tap-canny."""


import requests


from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable


from singer_sdk.streams import RESTStream



from singer_sdk.authenticators import (
    APIAuthenticatorBase,
    SimpleAuthenticator
)

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
        """Return a dictionary of values to be used in URL parameterization.

        If paging is supported, developers may override this method with specific paging
        logic.
        """
        params = {}
        return params

    def prepare_request_payload(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
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

    schema = PropertiesList(
        Property("id", StringType),
        Property("created", DateTimeType),
        Property("isPrivate", BooleanType),
        Property("name", StringType),
        Property("postCount", IntegerType),
        Property("token", StringType),
        Property("url", StringType),
    ).to_dict()


class ChangelogEntriesStream(CannyStream):
    """Changelog Entries stream class."""

    name = "changelog entries"

    path = "/entries/list"

    primary_keys = ["id"]
    replication_key = "lastSaved"

    #need to understand structure
    """   schema = PropertiesList(
    ).to_dict()"""

class CommentsStream(CannyStream):
    """Comments stream class."""

    name = "comments"

    path = "/comments/list"

    primary_keys = ["id"]
    #need to understand nested structure
    #replication_key = "created"

    """    schema = PropertiesList(
    ).to_dict()"""


class PostsStream(CannyStream):
    """Posts stream class."""

    name = "posts"

    path = "/posts/list"
    #need to understand nested structure
    """   primary_keys = ["id"]
    replication_key = "created"

    schema = PropertiesList(
    ).to_dict()"""


class StatusChangesStream(CannyStream):
    """Status Changes stream class."""

    name = "status changes"

    path = "/status_changes/list"

    primary_keys = ["id"]
    replication_key = "created"
    #need to understand nested structure
    """    schema = PropertiesList(
    ).to_dict()"""


class TagsStream(CannyStream):
    """Tags stream class."""

    name = "tags"

    path = "/tags/list"

    primary_keys = ["id"]
    replication_key = "created"

    # schema = PropertiesList(
    #     Property("id", StringType),
    #     Property("board", ObjectType),
    #     Property("created", DateTimeType),
    #     Property("name", StringType),
    #     Property("postCount", IntegerType),
    #     Property("url", StringType),
    # ).to_dict()


class VotesStream(CannyStream):
    """Votes stream class."""

    name = "votes"

    path = "/votes/list"

    primary_keys = ["id"]
    replication_key = "created"

    # schema = PropertiesList(
    #     Property("id", StringType),
    #     Property("board", ObjectType),
    #     Property("by", ObjectType),
    #     Property("created", DateTimeType),
    #     Property("post", ObjectType),
    #     Property("voter", ObjectType),
    #     Property("zenDeskTicket", ObjectType),
    # ).to_dict()