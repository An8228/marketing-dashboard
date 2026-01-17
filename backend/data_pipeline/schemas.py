# backend/data_pipeline/schemas.py

from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field


class EventType(str, Enum):
    CAMPAIGN_SENT = "campaign_sent"
    EMAIL_OPENED = "email_opened"
    LINK_CLICKED = "link_clicked"
    CONVERSION = "conversion"


class RawEvent(BaseModel):
    """
    Represents a single raw engagement event.
    Raw events are immutable and privacy-safe.
    """

    user_hash: str = Field(..., description="Anonymized user identifier")
    campaign_id: int
    event_type: EventType
    channel: str = Field(..., description="email, sms, push, etc.")
    timestamp: datetime
