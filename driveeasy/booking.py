from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from threading import RLock
from uuid import uuid4


HOLD_DURATION = timedelta(minutes=15)


class BookingConflictError(Exception):
    """The vehicle is unavailable for the requested period."""


@dataclass(frozen=True)
class BookingHold:
    hold_id: str
    vehicle_id: str
    rental_start: datetime
    rental_end: datetime
    expires_at: datetime


class BookingService:
    def __init__(self):
        self._holds: dict[str, BookingHold] = {}
        self._lock = RLock()

    def create_hold(
        self,
        vehicle_id: str,
        rental_start: datetime,
        rental_end: datetime,
        now: datetime | None = None,
    ) -> BookingHold:

        if not vehicle_id:
            raise ValueError("Vehicle ID is required")

        if rental_start.tzinfo is None or rental_end.tzinfo is None:
            raise ValueError("Rental dates must include a timezone")

        if rental_start >= rental_end:
            raise ValueError("Invalid rental period")

        now = now if now is not None else datetime.now(timezone.utc)

        if now.tzinfo is None:
            raise ValueError("Current time must include a timezone")

        with self._lock:
            for hold in self._holds.values():
                if hold.vehicle_id != vehicle_id:
                    continue

                if hold.expires_at <= now:
                    continue

                overlaps = (
                    rental_start < hold.rental_end
                    and hold.rental_start < rental_end
                )

                if overlaps:
                    raise BookingConflictError(
                        "Vehicle already has an active hold"
                    )

            hold = BookingHold(
                hold_id=str(uuid4()),
                vehicle_id=vehicle_id,
                rental_start=rental_start,
                rental_end=rental_end,
                expires_at=now + HOLD_DURATION,
            )

            self._holds[hold.hold_id] = hold
            return hold
