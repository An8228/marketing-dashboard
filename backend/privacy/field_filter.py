# backend/privacy/field_filter.py

# Defines which response fields each role is allowed to see
ROLE_FIELD_ACCESS = {
    "admin": {
        "campaign_id",
        "channel",
        "engagement_score",
        "timestamp",
    },
    "manager": {
        "campaign_id",
        "channel",
        "engagement_score",
    },
    "analyst": {
        "campaign_id",
        "engagement_score",
    },
}


def filter_response_fields(data: dict, role: str) -> dict:
    """
    Filters response data based on the user's role.

    Even if a user can access an endpoint, they may not
    be allowed to see all fields in the response.
    """
    allowed_fields = ROLE_FIELD_ACCESS.get(role, set())

    # Return only fields the role is allowed to see
    return {
        key: value
        for key, value in data.items()
        if key in allowed_fields
    }
