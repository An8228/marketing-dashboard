# backend/data_pipeline/raw_events.py

from typing import List
from backend.data_pipeline.schemas import RawEvent


class RawEventStore:
    """
    In-memory raw event store (Phase 3 prototype).

    - Append-only
    - No updates
    - No deletes

    In production, this would be a database or event log.
    """

    def __init__(self):
        self._events: List[RawEvent] = []

    def add_event(self, event: RawEvent) -> None:
        """
        Store a raw engagement event.
        """
        self._events.append(event)

    def get_all_events(self) -> List[RawEvent]:
        """
        Return all raw events (read-only).
        """
        return list(self._events)
