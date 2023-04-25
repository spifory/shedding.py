from __future__ import annotations

from typing import TYPE_CHECKING

from ._http import request

if TYPE_CHECKING:
    from .types.allowance import Allowance

__all__ = ("get_allowance",)

async def get_allowance(
    *,
    authorisation_token: str,
) -> Allowance:
    """
    Gets the current allowance/quota of requests that can be made.
    This does not count towards the allowance.

    Parameters
    ----------
    authorisation_token: :class:`str`
        The authorisation token to send requests with.

    Returns
    -------
    :class:`.Allowance`
        The quota of the amount of requests that can be made.

    .. versionadded:: 1.0
    """
    data = await request(
        "/api_allowance",
        authorisation_token=authorisation_token,
    )
    return data["allowance"]