# backend/privacy/safe_response.py

from typing import Optional

from backend.privacy.anonymizer import anonymize_user_id
from backend.privacy.field_filter import filter_response_fields


def build_safe_analytics_response(
    raw_data: dict,
    role: str,
    user_id: Optional[int] = None,
) -> dict:
    """
    Converts raw analytics data into a privacy-safe API response.

    Enforces:
    - User anonymization
    - Removal of unsafe fields
    - Role-based field visibility
    """
    # Copy to avoid mutating original data
    safe_data = raw_data.copy()

    # Anonymize user reference if applicable
    if user_id is not None:
        safe_data["user_hash"] = anonymize_user_id(user_id)

    # Explicitly remove unsafe fields (defensive)
    unsafe_fields = {"user_id", "email", "username"}
    for field in unsafe_fields:
        safe_data.pop(field, None)

    # Apply role-based field filtering
    safe_data = filter_response_fields(safe_data, role)

    return safe_data
