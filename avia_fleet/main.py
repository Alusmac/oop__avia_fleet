from .models.passenger import PassengerPlane
from .models.cargo import CargoPlane
from .models.military import MilitaryJet

from .exceptions.custom_errors import (
    AviaFleetException,
    OverloadCargoError,
    MaintenanceRequiredError,
)
from .utils.introspection import analyze_object, dynamic_call
from .utils.serialization import FleetDataManager
from .core.metaclasses import AircraftAutoRegisterMeta


def demonstrate_fleet() -> list:
    """Create and demonstrate the aircraft fleet."""
    print("\n=== 1. AIRCRAFT FLEET ===")

    fleet = [
        PassengerPlane("UR-12345", 180, 120),
        CargoPlane("UR-23456", 50, 20),
        MilitaryJet("UR-34567"),
    ]

    for aircraft in fleet:
        print(aircraft)

    return fleet


def demonstrate_flights(fleet: list) -> None:
    """Demonstrate aircraft flight operations."""
    print("\n=== 2. FLIGHT OPERATIONS ===")

    for aircraft in fleet:
        try:
            print(aircraft.takeoff())
            print(aircraft.fly(800))
            print(aircraft.land())
        except MaintenanceRequiredError as error:
            print(f"Flight unavailable: {error}")
        except ValueError as error:
            print(f"Invalid flight: {error}")


def demonstrate_cargo(fleet: list) -> None:
    """Demonstrate cargo loading and exception handling."""
    print("\n=== 3. CARGO MANAGEMENT ===")

    cargo_plane = fleet[1]

    try:
        print(cargo_plane.load_cargo(10))
        print(cargo_plane.load_cargo(100))
    except OverloadCargoError as error:
        print(f"Cargo error: {error}")


def demonstrate_maintenance(fleet: list) -> None:
    """Demonstrate maintenance operations."""
    print("\n=== 4. MAINTENANCE ===")

    military_jet = fleet[2]

    print(military_jet.eject())
    print("Serviceable:", military_jet.is_serviceable())

    try:
        print(military_jet.takeoff())
    except MaintenanceRequiredError as error:
        print(f"Maintenance error: {error}")

    print(military_jet.perform_maintenance())
    print("Serviceable:", military_jet.is_serviceable())


def demonstrate_introspection(fleet: list) -> None:
    """Demonstrate introspection and dynamic method calls."""
    print("\n=== 5. INTROSPECTION ===")

    passenger_plane = fleet[0]

    print(analyze_object(passenger_plane))
    print(dynamic_call(passenger_plane, "takeoff"))


def demonstrate_registration() -> None:
    """Display automatically registered aircraft classes."""
    print("\n=== 6. AUTOMATIC REGISTRATION ===")

    for name in AircraftAutoRegisterMeta._registry:
        print(name)


def demonstrate_serialization(fleet: list) -> None:
    """Save and load the aircraft fleet."""
    print("\n=== 7. JSON SERIALIZATION ===")

    filename = "fleet_data.json"

    FleetDataManager.save_fleet(fleet, filename)
    print(f"Fleet saved to {filename}")

    loaded_fleet = FleetDataManager.load_fleet(filename)

    print("Loaded aircraft:")
    for aircraft in loaded_fleet:
        print(aircraft)


def main() -> None:
    """Run the complete AviaFleet demonstration."""
    try:
        fleet = demonstrate_fleet()

        demonstrate_flights(fleet)
        demonstrate_cargo(fleet)
        demonstrate_maintenance(fleet)
        demonstrate_introspection(fleet)
        demonstrate_registration()
        demonstrate_serialization(fleet)

    except AviaFleetException as error:
        print(f"AviaFleet error: {error}")


if __name__ == "__main__":
    main()
