class AviaFleetException(Exception):
    """Base exception for the AviaFleet system."""
    pass


class InvalidTailNumberError(AviaFleetException):
    """Raised when an aircraft tail number is invalid."""
    pass


class OverloadCargoError(AviaFleetException):
    """Raised when cargo exceeds the aircraft payload capacity."""
    pass


class MaintenanceRequiredError(AviaFleetException):
    """Raised when an unserviceable aircraft is sent on a flight."""
    pass
