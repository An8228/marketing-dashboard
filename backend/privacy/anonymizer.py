# backend/privacy/anonymizer.py

import hashlib
import os

# Temporary dev salt (move to .env in production)
ANONYMIZATION_SALT = os.getenv(
    "ANONYMIZATION_SALT",
    "dev_salt_change_later"
)


def anonymize_user_id(user_id: int) -> str:
    """
    Convert a raw user ID into a deterministic anonymized hash.

    - Same input → same output
    - One-way (cannot be reversed)
    - Safe for analytics and dashboards
    """
    raw_value = f"{user_id}{ANONYMIZATION_SALT}"
    return hashlib.sha256(raw_value.encode()).hexdigest()

