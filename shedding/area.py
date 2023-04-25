from __future__ import annotations

from typing import TYPE_CHECKING

from ._http import request

if TYPE_CHECKING:
    from typing import List, Literal, Optional

    from .types.area import AreaInformation, AreaNearby, AreaSearch

__all__ = ("get_area_information", "search_areas", "get_nearby_areas",)

async def get_area_information(
    *,
    authorisation_token: str,
    id: str,
    test: Optional[Literal["current", "future"]] = None
) -> AreaInformation:
    """
    Gets the current events, schedule, and name/region of the requested area.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.
    id: :class:`str`
        The area's ID.
    test: Optional[Literal[:class:`str`]]
        Whether there should be test events as an ongoining, or future.

        By default, this will return accurate information instead of test information
        if this parameters is not provided.

    Returns
    -------
    :class:`.AreaInformation`
        The information gathered for the area

    .. versionadded:: 1.0
    """
    url = f"/area?id={id}"

    if test is not None:
        url += f"&test={test}"

    data = await request(
        url,
        authorisation_token=authorisation_token,
    )

    return data  # type: ignore


async def search_areas(
    *,
    authorisation_token: str,
    text: str,
) -> List[AreaSearch]:
    """
    Searches for areas that match the text provided.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.
    text: :class:`str`
        The text to search for.

    Returns
    -------
    :class:`.AreaSearch`
        The information gathered for the area

    .. versionadded:: 1.0
    """
    data = await request(
        f"/areas_search?text={text}",
        authorisation_token=authorisation_token,
    )
    return data["areas"]


async def get_nearby_areas(
    *,
    authorisation_token: str,
    latitude: float,
    longitude: float,
) -> List[AreaNearby]:
    """
    Gets the current events, schedule, and name/region of the requested area.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.
    latitude: :class:`float`
        The latitude of the area.

        .. note::
            This is known as ``lat`` on the API.

    longitude: :class:`float`
        The longitude of the area.

        .. note::
            This is known as ``lon`` on the API.

    Returns
    -------
    :class:`.AreaNearby`
        The information gathered for the area

    .. versionadded:: 1.0
    """
    data = await request(
        f"/areas_nearby?lat={latitude}&lon={longitude}",
        authorisation_token=authorisation_token,
    )
    return data["areas"]