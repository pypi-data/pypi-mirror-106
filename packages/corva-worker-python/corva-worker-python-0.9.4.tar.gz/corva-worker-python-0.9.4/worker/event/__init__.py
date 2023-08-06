import abc
from enum import Enum


class EventType(Enum):
    SCHEDULER = "scheduler"
    WITS_STREAM = "wits_stream"


class Event(abc.ABC):
    """An event class that holds the events of a single asset_id."""
    def __init__(self, event_type: EventType):
        self.event_type: EventType = event_type

        self.asset_id: int = None
        self.records = []

    def add_records(self, new_records: list) -> None:
        self.records.extend(new_records)

    @abc.abstractmethod
    def complete_event(self, api) -> None:
        raise NotImplementedError

    def __len__(self):
        return len(self.records)

    def __getitem__(self, index: int):
        return self.records[index]
