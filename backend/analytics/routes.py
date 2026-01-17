# backend/analytics/routes.py

from fastapi import APIRouter, Depends

from backend.analytics.schemas import CampaignAnalyticsResponse
from backend.auth.dependencies import get_current_user
from backend.auth.dependencies import require_role


from backend.data_pipeline.raw_events import RawEventStore
from backend.data_pipeline.aggregator import AnalyticsAggregator
from backend.privacy.safe_response import build_safe_analytics_response

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

# Phase 4 prototype: in-memory pipeline
event_store = RawEventStore()
aggregator = AnalyticsAggregator(event_store)


@router.get(
    "/campaigns",
    response_model=CampaignAnalyticsResponse,
)
def get_campaign_analytics(
    current_user=Depends(get_current_user),
):
    """
    Return aggregated campaign analytics.

    Roles allowed:
    - admin
    - manager
    - analyst
    """

    # RBAC enforcement
    require_role(current_user, ["admin", "manager", "analyst"])

    # Build analytics from Phase 3
    raw_metrics = aggregator.build_campaign_analytics()

    # Apply Phase 2 privacy + field-level filtering
    safe_metrics = {}
    for campaign_id, metrics in raw_metrics.items():
        safe_metrics[campaign_id] = build_safe_analytics_response(
            raw_data=metrics,
            role=current_user.role,
        )

    return {"campaigns": safe_metrics}
