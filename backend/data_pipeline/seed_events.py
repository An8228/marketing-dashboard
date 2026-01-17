# backend/data_pipeline/seed_events.py

from datetime import datetime

from backend.data_pipeline.raw_events import RawEventStore
from backend.data_pipeline.schemas import RawEvent, EventType

def seed_events(store: RawEventStore):
    events = [
        RawEvent("user1", 1, EventType.CAMPAIGN_SENT, "email", datetime.utcnow()),
        RawEvent("user1", 1, EventType.EMAIL_OPENED, "email", datetime.utcnow()),
        RawEvent("user1", 1, EventType.LINK_CLICKED, "email", datetime.utcnow()),
        RawEvent("user1", 1, EventType.CONVERSION, "email", datetime.utcnow()),

        RawEvent("user2", 1, EventType.CAMPAIGN_SENT, "email", datetime.utcnow()),
        RawEvent("user2", 1, EventType.EMAIL_OPENED, "email", datetime.utcnow()),

        RawEvent("user3", 2, EventType.CAMPAIGN_SENT, "sms", datetime.utcnow()),
    ]

    for event in events:
        store.add_event(event)
