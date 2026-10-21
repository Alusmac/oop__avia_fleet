from ..core.base_aircraft import AbstractAircraft
from ..exceptions.custom_errors import (
    OverloadCargoError,
    MaintenanceRequiredError,
)


class CargoPlane(AbstractAircraft):
    """Cargo aircraft for transporting freight."""

    def __init__(
            self,
            tail_number: str,
            max_payload_tons: float,
            current_payload_tons: float = 0.0,
            fuel_level: float = 100.0,
            flight_hours: float = 0.0,
    ) -> None:
        super().__init__(tail_number, fuel_level, flight_hours)

        if max_payload_tons <= 0:
            raise ValueError("Maximum payload must be positive.")

        if current_payload_tons < 0:
            raise ValueError("Cargo weight cannot be negative.")

        if current_payload_tons > max_payload_tons:
            raise OverloadCargoError(
                "Initial cargo exceeds maximum payload."
            )

        self.max_payload_tons = max_payload_tons
        self.current_payload_tons = current_payload_tons
        self._serviceable = True

    def load_cargo(self, weight: float) -> str:
        """Load cargo if the aircraft has enough capacity."""
        if weight <= 0:
            raise ValueError("Cargo weight must be positive.")

        total_weight = self.current_payload_tons + weight

        if total_weight > self.max_payload_tons:
            raise OverloadCargoError(
                f"Cannot load {weight} tons. "
                f"Maximum payload: {self.max_payload_tons} tons."
            )

        self.current_payload_tons = total_weight

        return (
            f"Loaded {weight} tons. "
            f"Total cargo: {self.current_payload_tons} tons."
        )

    def takeoff(self) -> str:
        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        return f"Cargo plane {self.tail_number} is taking off."

    def land(self) -> str:
        return f"Cargo plane {self.tail_number} has landed."

    def fly(self, distance: float) -> str:
        if distance <= 0:
            raise ValueError("Flight distance must be positive.")

        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        self._flight_hours += distance / 750

        return (
            f"Cargo plane {self.tail_number} flew "
            f"{distance} km with {self.current_payload_tons} tons of cargo."
        )

    def perform_maintenance(self) -> str:
        self._serviceable = True
        return f"Maintenance completed for {self.tail_number}."

    def is_serviceable(self) -> bool:
        return self._serviceable
