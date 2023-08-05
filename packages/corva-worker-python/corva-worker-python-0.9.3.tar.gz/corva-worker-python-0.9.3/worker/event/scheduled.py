from typing import Union, List

from worker.event import Event, EventType


class SingleScheduledEvent:
    def __init__(self, single_stream_event: dict):
        self.asset_id = single_stream_event.get('asset_id') or 0

        self.start_time = single_stream_event.get('schedule_start', 0) / 1000
        self.end_time = single_stream_event.get('schedule_end', 0) / 1000
        self.schedule_id = single_stream_event.get('schedule')

    def complete_event(self, api) -> None:
        """Sets schedule as completed."""
        if not self.schedule_id:
            return

        api.post(path=f'/scheduler/{self.schedule_id}/completed')


class ScheduledEvent(Event):
    """A scheduled event class that holds the events of a single asset_id."""
    def __init__(self, new_records: Union[SingleScheduledEvent, List[SingleScheduledEvent]]):
        super().__init__(EventType.SCHEDULER)

        if new_records:
            self.add_records(new_records)

    def add_records(self, new_records: Union[SingleScheduledEvent, List[SingleScheduledEvent]]):
        if isinstance(new_records, SingleScheduledEvent):
            new_records = [new_records]

        if not self.records:
            self.asset_id = new_records[0].asset_id

        super().add_records(new_records)

    def complete_event(self, api) -> None:
        for each in self.records:
            each.complete_event(api)
