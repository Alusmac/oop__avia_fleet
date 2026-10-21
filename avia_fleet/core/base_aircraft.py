from .interfaces import IFlyable, IMaintainable
from .metaclasses import AircraftAutoRegisterMeta
from ..utils.validators import validate_tail_number


class AbstractAircraft(IFlyable,IMaintainable,metaclass=AircraftAutoRegisterMeta,):
    """Abstract base class for all aircraft."""

    def __init__(self,tail_number: str,fuel_level: float = 100.0,flight_hours: float = 0.0,) -> None:
        self.__tail_number = tail_number
        self.fuel_level = fuel_level

        if flight_hours < 0:
            raise ValueError("Flight hours cannot be negative.")

        self._flight_hours = float(flight_hours)

    @property
    def tail_number(self) -> str:
        """Return the aircraft tail number."""
        return self.__tail_number

    @tail_number.setter
    def tail_number(self, value: str) -> None:
        if not validate_tail_number(value):
            from ..exceptions.custom_errors import (
                InvalidTailNumberError,
            )
            raise InvalidTailNumberError(
                f"Invalid tail number: {value}"
            )

        self.__tail_number = value

    @property
    def fuel_level(self) -> float:
        """Return the current fuel level."""
        return self._fuel_level

    @fuel_level.setter
    def fuel_level(self, value: float) -> None:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError("Fuel level must be a number.")

        if not 0 <= value <= 100:
            raise ValueError("Fuel level must be between 0 and 100.")

        self._fuel_level = float(value)

    @property
    def flight_hours(self) -> float:
        """Return the total flight hours."""
        return self._flight_hours

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(tail_number={self.tail_number})"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"tail_number={self.tail_number!r}, "
            f"fuel_level={self.fuel_level!r}, "
            f"flight_hours={self.flight_hours!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AbstractAircraft):
            return NotImplemented

        return self.tail_number == other.tail_number

    def __len__(self) -> int:
        """Return whole flight hours, as required by len()."""
        return int(self._flight_hours)
