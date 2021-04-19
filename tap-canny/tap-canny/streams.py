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

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]


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
        starting_datetime = self.get_starting_timestamp(partition)
        if starting_datetime:
            params["updated"] = starting_datetime
        return params



    @property
    def authenticator(self) -> APIAuthenticatorBase:
        return SimpleAuthenticator(
            stream=self,
            # Needs to be query parameter instead of header
            auth_headers={
                "apiKey": self.config.get("apiKey")
            }
        )

    # Alternatively, you can pass auth tokens directly within http_headers:
    # @property
    # def http_headers(self) -> dict:
    #     headers = {}
    #     if "user_agent" in self.config:
    #         headers["User-Agent"] = self.config.get("user_agent")
    #     headers["Private-Token"] = self.config.get("auth_token")
    #     return headers


class BoardsStream(CannyStream):
    """Boards stream class."""

    name = "boards"

    path = "/boards/list"

    primary_keys = ["id"]
    replication_key = "created"

    schema = PropertiesList(
        Property("boards", 
                ArrayType(
                    ObjectType(
                        Property("id", StringType),
                        Property("created", DateTimeType),
                        Property("isPrivate", BooleanType),
                        Property("name", StringType),
                        Property("postCount", IntegerType),
                        Property("token", StringType),
                        Property("url", StringType),
                    )
                )
        ),
    ).to_dict()


class ChangelogEntriesStream(CannyStream):
    """Changelog Entries stream class."""

    name = "changelog entries"

    path = "/entries/list"

    primary_keys = ["id"]
    replication_key = "lastSaved"

    schema = PropertiesList(
        Property("entries", 
                ArrayType(
                    ObjectType(
                        Property("id", StringType),
                        Property("created", DateTimeType),
                        Property("labels", ArrayType(StringType)),
                        Property("lastSaved", DateTimeType),
                        Property("markdownDetails", StringType),
                        Property("plaintextDetails", StringType),
                        Property("posts",
                                ArrayType(
                                    ObjectType(
                                        Property("category",
                                                ObjectType(
                                                    Property("id", StringType),
                                                    Property("name", StringType),
                                                    Property("postCount", IntegerType),
                                                    Property("url", StringType),
                                                )
                                        ),
                                        Property("commentCount", IntegerType),
                                        Property("id", StringType),
                                        Property("imageURLs", ArrayType(StringType)),
                                        Property("jira",
                                                ObjectType(
                                                    Property("linkedIssues",
                                                            ArrayType(
                                                                ObjectType(
                                                                    Property("id", StringType),
                                                                    Property("key", StringType),
                                                                    Property("url", StringType),
                                                                )
                                                            )
                                                    )
                                                )
                                        ),
                                        Property("score", IntegerType),
                                        Property("status", StringType),
                                        Property("tags", 
                                                ArrayType(
                                                    ObjectType(
                                                        Property("id", StringType),
                                                        Property("board",
                                                                ObjectType(
                                                                    Property("id", StringType),
                                                                    Property("created", DateTimeType),
                                                                    Property("isPrivate", BooleanType),
                                                                    Property("name", StringType),
                                                                    Property("postCount", IntegerType),
                                                                    Property("token", StringType),
                                                                    Property("url", StringType),
                                                                )
                                                        ),
                                                        Property("created", DateTimeType),
                                                        Property("name", StringType),
                                                        Property("postCount", IntegerType),
                                                        Property("url", StringType),
                                                    )
                                                )
                                        ),
                                        Property("title", StringType),
                                        Property("url", StringType),
                                    )
                                )
                        ),
                        Property("publishedAt", DateTimeType),
                        Property("scheduledFor", DateTimeType),
                        Property("status", StringType),
                        Property("title", StringType),
                        Property("types", ArrayType(StringType)),
                        Property("url", StringType),
                    )
                )
        ),
    ).to_dict()

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

    schema = PropertiesList(
        Property("hasMore", BooleanType),
        Property("tags", 
                ArrayType(
                    ObjectType(
                        Property("id", StringType),
                        Property("board",
                                ObjectType(
                                    Property("id", StringType),
                                    Property("created", DateTimeType),
                                    Property("isPrivate", BooleanType),
                                    Property("name", StringType),
                                    Property("postCount", IntegerType),
                                    Property("token", StringType),
                                    Property("url", StringType),
                                )
                        ),
                        Property("created", DateTimeType),
                        Property("name", StringType),
                        Property("postCount", IntegerType),
                        Property("url", StringType),
                    )
                )
        ),
    ).to_dict()


class VotesStream(CannyStream):
    """Votes stream class."""

    name = "votes"

    path = "/votes/list"

    primary_keys = ["id"]
    replication_key = "created"

    schema = PropertiesList(
        Property("hasMore", BooleanType),
        Property("votes",
                ArrayType(
                    ObjectType(
                        Property("id", StringType),
                        Property("board",
                            ObjectType(
                                Property("id", StringType),
                                Property("created", DateTimeType),
                                Property("isPrivate", BooleanType),
                                Property("name", StringType),
                                Property("postCount", IntegerType),
                                Property("token", StringType),
                                Property("url", StringType),
                        )),
                        Property("by", 
                                ObjectType(
                                    Property("id", StringType),
                                    Property("created", DateTimeType),
                                    Property("isPrivate", BooleanType),
                                    Property("name", StringType),
                                    Property("postCount", IntegerType),
                                    Property("token", StringType),
                                    Property("url", StringType),
                                )
                        ),
                        Property("created", DateTimeType),
                        Property("post",
                                ObjectType(
                                    Property("category",
                                            ObjectType(
                                                Property("id", StringType),
                                                Property("name", StringType),
                                                Property("postCount", IntegerType),
                                                Property("url", StringType),
                                            )
                                    ),
                                    Property("commentCount", IntegerType),
                                    Property("id", StringType),
                                    Property("imageURLs", ArrayType(StringType)),
                                    Property("jira",
                                            ObjectType(
                                                Property("linkedIssues",
                                                        ArrayType(
                                                            ObjectType(
                                                                Property("id", StringType),
                                                                Property("key", StringType),
                                                                Property("url", StringType),
                                                            )
                                                        )
                                                )
                                            )
                                    ),
                                    Property("score", IntegerType),
                                    Property("status", StringType),
                                    Property("tags", 
                                            ArrayType(
                                                ObjectType(
                                                    Property("id", StringType),
                                                    Property("board",
                                                            ObjectType(
                                                                Property("id", StringType),
                                                                Property("created", DateTimeType),
                                                                Property("isPrivate", BooleanType),
                                                                Property("name", StringType),
                                                                Property("postCount", IntegerType),
                                                                Property("token", StringType),
                                                                Property("url", StringType),
                                                            )
                                                    ),
                                                    Property("created", DateTimeType),
                                                    Property("name", StringType),
                                                    Property("postCount", IntegerType),
                                                    Property("url", StringType),
                                                )
                                            )
                                    ),
                                    Property("title", StringType),
                                    Property("url", StringType),
                                )
                        ),
                        Property("voter", 
                                ObjectType(
                                    Property("id", StringType),
                                    Property("created", DateTimeType),
                                    Property("isPrivate", BooleanType),
                                    Property("name", StringType),
                                    Property("postCount", IntegerType),
                                    Property("token", StringType),
                                    Property("url", StringType),
                                )
                        ),
                        Property("zenDeskTicket",
                                ObjectType(
                                    Property("url", StringType),
                                    Property("id", IntegerType),
                                    Property("created", DateTimeType),
                                    Property("subject", StringType),
                                    Property("description", StringType),
                                )
                        ),
                    )
                )
            ),
    ).to_dict()