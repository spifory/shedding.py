from typing import TypedDict

__all__ = ("Topic",)


class Topic(TypedDict):
    """Type annotation for a topic.
    
    Parameters
    ----------
    active: :class:`str`
        The date for when the topic was last active.
    body: :class:`str`
        The body of the topic.
    category: :class:`str`
        The category for the topic.
    distance: :class:`int`
        The distance from the topic author.
    followers: :class:`int`
        The amount of followers the topic has.
    timestamp: :class:`int`
        The timestamp for when the topic was created.
    """
    active: str
    body: str
    # not very easy to know what categories are avaliable
    # as I have been told that they change over time
    # so I will just leave it as a string
    category: str
    distance: int
    followers: int
    timestamp: int
