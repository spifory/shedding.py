from typing import List, TypedDict

__all__ = ("NextStage", "Status",)

class NextStage(TypedDict):
    """Type annotation for upcoming stage(s) in the load shedding schedule.
    
    Parameters
    ----------
    stage: :class:`str`
        The upcoming stage number.
    stage_start_timestamp: :class:`str`
        The timestamp for when the stage starts.
    """
    stage: str
    stage_start_timestamp: str


class Status(TypedDict):
    """Type annotation for the current loadshedding status.
    
    Parameters
    ----------
    name: :class:`str`
        The name of the current stage.
    next_stages: List[:class:`NextStage`]
        The upcoming stages in the load shedding schedule.
    stage: :class:`str`
        The current stage number.
    stage_updated: :class:`str`
        The timestamp for when the stage was updated.
    """
    name: str
    next_stages: List[NextStage]
    stage: str
    stage_updated: str
