from typing import Literal, TypedDict

__all__ = ("RequestReAllocationType", "Allowance",)

RequestReAllocationType = Literal["daily"] # really not sure about this name

class Allowance(TypedDict):
    """Type annotations for the 
    `/api_allowance </https://documenter.getpostman.com/view/1296288/UzQuNk3E#10647b8e-c839-4d56-82a2-d9a406ae4f18>`_ route
    
    Parameters
    ----------
    count: :class:`int`
        The amount of usable requests left.
    limit: :class:`int`
        The limit of requests that can be made.
    type: Literal[:class:`str`]
        The request re-allocation type. This is always ``daily``
    """  # noqa: E501 The hyperlink is too long
    count: int
    limit: int
    type: RequestReAllocationType
