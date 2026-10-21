from abc import ABC, abstractmethod


class IFlyable(ABC):
    """Interface for aircraft flight operations."""

    @abstractmethod
    def takeoff(self) -> str:
        """Take off."""
        pass

    @abstractmethod
    def land(self) -> str:
        """Land."""
        pass

    @abstractmethod
    def fly(self, distance: float) -> str:
        """Fly a specified distance."""
        pass


class IMaintainable(ABC):
    """Interface for aircraft maintenance operations."""

    @abstractmethod
    def perform_maintenance(self) -> str:
        """Perform aircraft maintenance."""
        pass

    @abstractmethod
    def is_serviceable(self) -> bool:
        """Check whether the aircraft is ready for operation."""
        pass
