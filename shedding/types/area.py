from typing import List, TypedDict

__all__ = (
    "AreaEvent",
    "AreaInformation",
    "AreaNearby",
    "AreaSchedule",
    "AreaScheduleDay",
    "AreaSearch",
    "BriefAreaInformation",
)

class AreaEvent(TypedDict):
    """Type annotation for an area's events.

    Parameters
    ----------
    end: :class:`str`
        The expected end time for this stage.
    note: :class:`str`
        The note of the event. This is usually the current load shedding stage.
    start: :class:`str`
        The expected start time for this stage.
    """
    end: str
    note: str
    start: str


class BriefAreaInformation(TypedDict):
    """Type annotation for the area's information in a brief form.

    This is mainly just a base for the 
    :class:`AreaInformation`, :class:`AreaSearch` and :class:`AreaNearby` types.

    Parameters
    ----------
    name: :class:`str`
        The name of the area.
    region: :class:`str`
        The region of the area.
    """
    name: str
    region: str


class AreaScheduleDay(TypedDict):
    """Type annotation for the a day in an area's schedule.

    Parameters
    ----------
    date: :class:`str`
        The date when the schedule takes place.
    name: :class:`str`
        The name of the day.
    stages: List[:class:`str`]
        The stages for the day.
    """
    date: str
    name: str
    stages: List[str]


class AreaSchedule(TypedDict):
    """Type annotation for an area's schedule.
    
    Parameters
    ----------
    days: List[:class:`AreaScheduleDay`]
        The days in the schedule.
    source: :class:`str`
        The source of the schedule.
        This is usually from `Eskom <https://loadshedding.eskom.co.za>`_.
    """
    days: List[AreaScheduleDay]
    source: str


class AreaSearch(BriefAreaInformation):
    """Type annotation for an area's search result.

    Parameters
    ----------
    id: :class:`str`
        The id of the area.
    """
    id: str


class AreaNearby(AreaSearch):
    """Type annotation for an area's nearby search result.

    Parameters
    ----------
    count: :class:`int`
        The amount of nearby areas.
    """
    count: int

class AreaInformation(TypedDict):
    """Type annotation for an area's information.
    
    This is the most detailed type for an area.
    
    Parameters
    ----------
    events: List[:class:`AreaEvent`]
        The events for the area.
    info: :class:`BriefAreaInformation`
        The brief information for the area.
    schedule: :class:`AreaSchedule`
        The schedule for the area.
    """
    events: List[AreaEvent]
    info: BriefAreaInformation
    schedule: AreaSchedule
