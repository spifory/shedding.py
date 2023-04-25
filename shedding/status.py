from __future__ import annotations

from typing import TYPE_CHECKING

from ._http import request

if TYPE_CHECKING:
    from typing import Literal

    from .types.status import Status

__all__ = ("get_status",)

async def get_status(
    *,
    authorisation_token: str,
    area: Literal["national", "capetown"] = "national",
) -> Status:
    """
    Gets the current load shedding status nationally or for certain municipalities
    mainly located in Cape Town.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.
    area: Literal[:class:`str`]
        The area to get the status for. This can be either ``national`` or ``capetown``

        .. note::
            This ``national`` status is known as the ``eskom`` status on the API.

    Returns
    -------
    :class:`.Status`
        The current load shedding status.

    .. versionadded:: 1.0
    """
    data = await request(
        "/status",
        authorisation_token=authorisation_token,
    )

    if area == "national":
        return data["status"]["eskom"]
    else:
        return data["status"]["capetown"]
