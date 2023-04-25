from __future__ import annotations

from typing import TYPE_CHECKING

from ._http import request

if TYPE_CHECKING:
    from typing import List

    from .types.topics import Topic

__all__ = ("get_topics_nearby",)


async def get_topics_nearby(
    *,
    authorisation_token: str,
    lattitude: float,
    longitude: float,
) -> List[Topic]:
    """
    Gets the topics nearby the lattitude and longitude provided.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.
    lattitude: :class:`float`
        The lattitude to get the topics for.

        .. note::
            This is known as ``lat`` on the API.

    longitude: :class:`float`
        The longitude to get the topics for.

        .. note::
            This is known as ``lon`` on the API.

    Returns
    -------
    List[:class:`.Topic`]
        The topics nearby the lattitude and longitude provided.

    .. versionadded:: 1.0
    """
    data = await request(
        f"/topics_nearby?lat={lattitude}&lon={longitude}",
        authorisation_token=authorisation_token,
    )
    return data["topics"]