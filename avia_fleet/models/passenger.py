from ..core.base_aircraft import AbstractAircraft
from ..exceptions.custom_errors import MaintenanceRequiredError


class PassengerPlane(AbstractAircraft):
    """Passenger aircraft for commercial transportation."""

    def __init__(
            self,
            tail_number: str,
            passengers_capacity: int,
            current_passengers: int = 0,
            fuel_level: float = 100.0,
            flight_hours: float = 0.0,
    ) -> None:
        super().__init__(tail_number, fuel_level, flight_hours)

        if passengers_capacity <= 0:
            raise ValueError("Passenger capacity must be positive.")

        if not 0 <= current_passengers <= passengers_capacity:
            raise ValueError(
                "Current passengers must be within aircraft capacity."
            )

        self.passengers_capacity = passengers_capacity
        self.current_passengers = current_passengers
        self._serviceable = True

    def takeoff(self) -> str:
        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        return f"Passenger plane {self.tail_number} is taking off."

    def land(self) -> str:
        return f"Passenger plane {self.tail_number} has landed."

    def fly(self, distance: float) -> str:
        if distance <= 0:
            raise ValueError("Flight distance must be positive.")

        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        self._flight_hours += distance / 800
        return (
            f"Passenger plane {self.tail_number} flew "
            f"{distance} km."
        )

    def perform_maintenance(self) -> str:
        self._serviceable = True
        return f"Maintenance completed for {self.tail_number}."

    def is_serviceable(self) -> bool:
        return self._serviceable
