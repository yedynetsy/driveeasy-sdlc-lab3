
from datetime import datetime, timedelta, timezone

import pytest

from driveeasy.booking import BookingService, BookingConflictError


NOW = datetime(2026, 11, 3, 10, 0, tzinfo=timezone.utc)
START = datetime(2026, 11, 5, 12, 0, tzinfo=timezone.utc)
END = START + timedelta(days=2)


def test_hold_expires_after_15_minutes():
    service = BookingService()

    hold = service.create_hold("CAR-001", START, END, now=NOW)

    assert hold.vehicle_id == "CAR-001"
    assert hold.expires_at == NOW + timedelta(minutes=15)


def test_cannot_hold_same_vehicle_twice():
    service = BookingService()

    service.create_hold("CAR-001", START, END, now=NOW)

    with pytest.raises(BookingConflictError):
        service.create_hold("CAR-001", START, END, now=NOW)


def test_vehicle_available_after_hold_expires():
    service = BookingService()

    service.create_hold("CAR-001", START, END, now=NOW)

    later = NOW + timedelta(minutes=16)
    new_hold = service.create_hold(
        "CAR-001", START, END, now=later
    )

    assert new_hold.vehicle_id == "CAR-001"


def test_cannot_hold_vehicle_with_blank_id():
    service = BookingService()

    with pytest.raises(ValueError, match="Vehicle ID is required"):
        service.create_hold("   ", START, END, now=NOW)
