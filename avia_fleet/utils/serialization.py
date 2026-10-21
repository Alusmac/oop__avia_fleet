import json
from pathlib import Path

from ..models.passenger import PassengerPlane
from ..models.cargo import CargoPlane
from ..models.military import MilitaryJet

FLEET_DATA_PATH = Path(__file__).resolve().parent.parent / "fleet_data.json"


class FleetDataManager:
    """Manage saving and loading aircraft fleet data."""

    @staticmethod
    def save_fleet(aircraft_list: list, filename: str = "fleet_data.json") -> None:
        """Save aircraft data to a JSON file."""
        fleet_data = []

        for aircraft in aircraft_list:
            data = {
                "type": aircraft.__class__.__name__,
                "tail_number": aircraft.tail_number,
                "fuel_level": aircraft.fuel_level,
                "flight_hours": aircraft.flight_hours,
            }

            if isinstance(aircraft, PassengerPlane):
                data["passengers_capacity"] = aircraft.passengers_capacity
                data["current_passengers"] = aircraft.current_passengers

            elif isinstance(aircraft, CargoPlane):
                data["max_payload_tons"] = aircraft.max_payload_tons
                data["current_payload_tons"] = aircraft.current_payload_tons

            fleet_data.append(data)

        path = FLEET_DATA_PATH
        with path.open("w", encoding="utf-8") as file:
            json.dump(fleet_data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def load_fleet(filename: str = "fleet_data.json") -> list:
        """Load aircraft data from a JSON file."""
        path = FLEET_DATA_PATH

        with path.open("r", encoding="utf-8") as file:
            fleet_data = json.load(file)

        aircraft_list = []

        for data in fleet_data:
            aircraft_type = data["type"]

            if aircraft_type == "PassengerPlane":
                aircraft = PassengerPlane(
                    tail_number=data["tail_number"],
                    passengers_capacity=data["passengers_capacity"],
                    current_passengers=data["current_passengers"],
                    fuel_level=data["fuel_level"],
                    flight_hours=data["flight_hours"],
                )

            elif aircraft_type == "CargoPlane":
                aircraft = CargoPlane(
                    tail_number=data["tail_number"],
                    max_payload_tons=data["max_payload_tons"],
                    current_payload_tons=data["current_payload_tons"],
                    fuel_level=data["fuel_level"],
                    flight_hours=data["flight_hours"],
                )

            elif aircraft_type == "MilitaryJet":
                aircraft = MilitaryJet(
                    tail_number=data["tail_number"],
                    fuel_level=data["fuel_level"],
                    flight_hours=data["flight_hours"],
                )

            else:
                raise ValueError(f"Unknown aircraft type: {aircraft_type}")

            aircraft_list.append(aircraft)

        return aircraft_list
