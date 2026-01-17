# backend/analytics/schemas.py

from pydantic import BaseModel
from typing import Dict


class CampaignMetrics(BaseModel):
    sent: int
    opens: int
    clicks: int
    conversions: int
    open_rate: float
    ctr: float
    conversion_rate: float
    engagement_score: float


class CampaignAnalyticsResponse(BaseModel):
    campaigns: Dict[int, CampaignMetrics]
