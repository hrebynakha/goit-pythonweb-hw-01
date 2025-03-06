"""Home work 1"""

from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)


class Vehicle:
    """Base ehicle class"""

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
    """Car base class"""

    def __init__(self, make: str, model: str, spec_region: str):
        self.make = make
        self.model = model
        self.spec_region = spec_region
        super().__init__(make, model, spec_region)


class Motorcycle(Vehicle):
    """Motorcycle base class"""

    def __init__(self, make: str, model: str, spec_region: str):
        self.make = make
        self.model = model
        self.spec_region = spec_region
        super().__init__(make, model, spec_region)


class VehicleFactory(ABC):
    """Base class for factory"""

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        """Abstartc method for car"""

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        """Abstartc method for motorcycle"""


class USVehicleFactory(VehicleFactory):
    """USVehicleFactory"""

    def __init__(
        self,
    ):
        self.spec_region = "US"
        super().__init__()

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


class EUVehicleFactory(VehicleFactory):
    """EUVehicleFactory"""

    def __init__(
        self,
    ):
        self.spec_region = "EU"
        super().__init__()

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec_region)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec_region)


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")

vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
