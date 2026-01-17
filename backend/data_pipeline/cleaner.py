# backend/data_pipeline/cleaner.py

from typing import List, Set, Tuple
from backend.data_pipeline.schemas import RawEvent


def clean_events(events: List[RawEvent]) -> List[RawEvent]:
    """
    Clean and validate raw events.

    Rules:
    - Remove duplicates
    - Reject events with missing or invalid fields
    - Preserve original event objects (do not mutate)
    """

    cleaned_events: List[RawEvent] = []
    seen_events: Set[Tuple] = set()

    for event in events:
        # Build a uniqueness key
        event_key = (
            event.user_hash,
            event.campaign_id,
            event.event_type,
            event.channel,
            event.timestamp,
        )

        # Skip duplicates
        if event_key in seen_events:
            continue

        # Basic validation checks
        if not event.user_hash:
            continue
        if not event.channel:
            continue
        if not event.timestamp:
            continue

        seen_events.add(event_key)
        cleaned_events.append(event)

    return cleaned_events
