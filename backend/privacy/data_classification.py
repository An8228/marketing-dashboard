# backend/privacy/data_classification.py

from enum import Enum


class DataSensitivity(str, Enum):
    PII = "pii"
    INDIRECT_IDENTIFIER = "indirect_identifier"
    ANALYTICS_SAFE = "analytics_safe"


# Central registry of fields and their sensitivity
DATA_FIELD_CLASSIFICATION = {
    # Direct identifiers (never exposed)
    "email": DataSensitivity.PII,
    "username": DataSensitivity.PII,

    # Indirect identifiers (must be anonymized)
    "user_id": DataSensitivity.INDIRECT_IDENTIFIER,

    # Analytics-safe fields
    "campaign_id": DataSensitivity.ANALYTICS_SAFE,
    "event_type": DataSensitivity.ANALYTICS_SAFE,
    "timestamp": DataSensitivity.ANALYTICS_SAFE,
    "channel": DataSensitivity.ANALYTICS_SAFE,
    "engagement_score": DataSensitivity.ANALYTICS_SAFE,
}
