from ..core.base_aircraft import AbstractAircraft
from ..exceptions.custom_errors import MaintenanceRequiredError


class WeaponSystemMixin:
    """Mixin providing weapon system functionality."""

    def activate_weapon_system(self) -> str:
        """Activate the aircraft weapon system."""
        return "Weapon system activated."

    def deactivate_weapon_system(self) -> str:
        """Deactivate the aircraft weapon system."""
        return "Weapon system deactivated."


class MilitaryJet(WeaponSystemMixin, AbstractAircraft):
    """Military jet with afterburner and ejection capabilities."""

    def __init__(
            self,
            tail_number: str,
            fuel_level: float = 100.0,
            flight_hours: float = 0.0,
    ) -> None:
        super().__init__(tail_number, fuel_level, flight_hours)
        self._serviceable = True
        self._afterburner_active = False

    def takeoff(self) -> str:
        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        return f"Military jet {self.tail_number} is taking off."

    def land(self) -> str:
        return f"Military jet {self.tail_number} has landed."

    def fly(self, distance: float) -> str:
        if distance <= 0:
            raise ValueError("Flight distance must be positive.")

        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        self._flight_hours += distance / 1200

        return (
            f"Military jet {self.tail_number} flew "
            f"{distance} km."
        )

    def activate_afterburner(self) -> str:
        if not self.is_serviceable():
            raise MaintenanceRequiredError(
                f"Aircraft {self.tail_number} requires maintenance."
            )

        self._afterburner_active = True
        self._fuel_level = max(0.0, self._fuel_level - 10.0)

        return "Afterburner activated. Fuel consumption increased."

    def eject(self) -> str:
        self._serviceable = False
        self._afterburner_active = False

        return f"Pilot of {self.tail_number} has ejected."

    def perform_maintenance(self) -> str:
        self._serviceable = True
        self._afterburner_active = False

        return f"Maintenance completed for {self.tail_number}."

    def is_serviceable(self) -> bool:
        return self._serviceable
