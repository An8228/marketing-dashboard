# backend/data_pipeline/aggregator.py

from typing import Dict, List

from backend.data_pipeline.raw_events import RawEventStore
from backend.data_pipeline.cleaner import clean_events
from backend.data_pipeline.metrics import compute_campaign_metrics


class AnalyticsAggregator:
    """
    Orchestrates the analytics pipeline:
    Raw Events -> Cleaned Events -> Metrics
    """

    def __init__(self, event_store: RawEventStore):
        self.event_store = event_store

    def build_campaign_analytics(self) -> Dict[int, Dict[str, float]]:
        """
        Build aggregated campaign analytics.

        This method is safe to be called by APIs.
        """
        # Step 1: Fetch raw events
        raw_events = self.event_store.get_all_events()

        # Step 2: Clean & validate
        cleaned_events = clean_events(raw_events)

        # Step 3: Compute metrics
        campaign_metrics = compute_campaign_metrics(cleaned_events)

        return campaign_metrics
