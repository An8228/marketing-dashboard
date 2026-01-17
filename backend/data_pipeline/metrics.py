# backend/data_pipeline/metrics.py

from typing import Dict, List
from collections import defaultdict

from backend.data_pipeline.schemas import RawEvent, EventType


def compute_campaign_metrics(
    events: List[RawEvent],
) -> Dict[int, Dict[str, float]]:
    """
    Compute engagement metrics per campaign.

    Returns:
    {
        campaign_id: {
            "sent": int,
            "opens": int,
            "clicks": int,
            "conversions": int,
            "open_rate": float,
            "ctr": float,
            "conversion_rate": float,
            "engagement_score": float
        }
    }
    """

    stats = defaultdict(lambda: {
        "sent": 0,
        "opens": 0,
        "clicks": 0,
        "conversions": 0,
    })

    # Count events
    for event in events:
        cid = event.campaign_id

        if event.event_type == EventType.CAMPAIGN_SENT:
            stats[cid]["sent"] += 1
        elif event.event_type == EventType.EMAIL_OPENED:
            stats[cid]["opens"] += 1
        elif event.event_type == EventType.LINK_CLICKED:
            stats[cid]["clicks"] += 1
        elif event.event_type == EventType.CONVERSION:
            stats[cid]["conversions"] += 1

    # Compute derived metrics
    results: Dict[int, Dict[str, float]] = {}

    for cid, values in stats.items():
        sent = values["sent"]
        opens = values["opens"]
        clicks = values["clicks"]
        conversions = values["conversions"]

        open_rate = opens / sent if sent > 0 else 0.0
        ctr = clicks / opens if opens > 0 else 0.0
        conversion_rate = conversions / clicks if clicks > 0 else 0.0

        # Simple weighted engagement score
        engagement_score = (
            opens * 1.0 +
            clicks * 2.0 +
            conversions * 3.0
        )

        results[cid] = {
            "sent": sent,
            "opens": opens,
            "clicks": clicks,
            "conversions": conversions,
            "open_rate": round(open_rate, 4),
            "ctr": round(ctr, 4),
            "conversion_rate": round(conversion_rate, 4),
            "engagement_score": engagement_score,
        }

    return results
