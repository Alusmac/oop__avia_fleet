from abc import ABCMeta


class AircraftAutoRegisterMeta(ABCMeta):
    """Metaclass for aircraft validation and registration."""

    _registry = {}

    def __new__(mcs, name, bases, namespace):
        """Create and register an aircraft class."""
        if not namespace.get("__doc__"):
            raise TypeError(f"Class {name} must have a docstring.")

        cls = super().__new__(mcs, name, bases, namespace)

        if name != "AbstractAircraft":
            mcs._registry[name] = cls

        return cls
