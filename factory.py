"""Home work 1"""

from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)


class Vehicle:
    """Base vehicle class"""

    def __init__(self, make: str, model: str, spec_region: str):
        self.make = make
        self.model = model
        self.spec_region = spec_region

    def start_engine(self) -> None:
        """Satrt engine method"""
        logging.info(
            "%s %s (%s Spec): Двигун запущено", self.make, self.model, self.spec_region
        )


class Car(Vehicle):
    """Car class"""


class Motorcycle(Vehicle):
    """Motorcycle class"""


class VehicleFactory(ABC):
    """Base class for factory"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        """Abstratc method for car"""

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Abstratc method for motorcycle"""


class USVehicleFactory(VehicleFactory):
    """US factory"""

    def __init__(
        self,
    ):
        self.spec_region = "US"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


class EUVehicleFactory(VehicleFactory):
    """EU factory"""

    def __init__(
        self,
    ):
        self.spec_region = "EU"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Toyota", "Corolla")

    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()
