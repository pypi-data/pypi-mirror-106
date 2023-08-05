import json
from typing import List, Union

from cached_property import cached_property

from worker.data.operations import get_data_by_path
from worker.event import Event, EventType
from worker.framework import constants


class StreamEvent(Event):
    """A stream event class that holds the events of a single asset_id."""
    def __init__(self, event: dict, is_posting_to_message_producer: bool = False):
        super().__init__(EventType.WITS_STREAM)

        self.metadata = event.get('metadata') or {}
        self.records = event.get('records') or []

        self.asset_id = 0
        if self.records:
            self.asset_id = self.records[0].get('asset_id')

        app_key = constants.get('global.stream_app_key')
        self.app_connection_id = get_data_by_path(
            self.metadata,
            f'apps.{app_key}.app_connection_id',
            func=int,
            default=None
        )

    @cached_property
    def is_posting_to_message_producer(self) -> bool:
        """
        Whether to post to message producer for the wits stream or not.
        If there is no lambda app following your app then this should be false,
        because this process is intracting with the API which slows the process down.
        """
        is_posting: bool = constants.get('global.post-to-message-producer', False)
        return is_posting

    @classmethod
    def merge(cls, events: List['StreamEvent']) -> Union['StreamEvent', None]:
        """Merge stream events of the same asset id into one"""
        if not events:
            return None

        merged_event = events[0]
        for each in events[1:]:
            merged_event.add(each)

        return merged_event

    def add(self, other: 'StreamEvent'):
        if self.asset_id != other.asset_id:
            raise Exception(f"Events of different assets can not be merged; {self.asset_id} and {other.asset_id}!")

        self.add_records(other.records)

    def build_message_producer_payload(self) -> dict:
        return {
            'app_connection_id': self.app_connection_id,
            'asset_id': self.asset_id,
            'data': self.records
        }

    def complete_event(self, api):
        if not self.is_posting_to_message_producer or not self.app_connection_id:
            return

        payload = self.build_message_producer_payload()
        api.post(path='/v1/message_producer', data=json.dumps(payload))
