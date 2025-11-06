from abc import ABC, abstractmethod
from typing import Any, Dict

class HeatPumpBase(ABC):
    """Abstract base class for heat pump implementations."""

    def __init__(self, name: str = "Heat Pump"):
        self.name = name
        print(f"{self.name} initialized.")


    @abstractmethod
    def set_status(self, ambient_temperature: float, target_temperature: float) -> None:
        """Set the operational status of the heat pump.

        Args:
            ambient_temperature: The ambient temperature in Celsius.
            target_temperature: The desired target temperature in Celsius.
        """
        pass


    @abstractmethod
    def get_status(self) -> Dict[str, Any]:
        """Retrieve the current status of the heat pump. 
            Includes COP, mode, target temperature, etc.

        Returns:
            A dictionary containing status information.
        """
        pass

    @abstractmethod
    def step(self) -> None:
        """Advance the heat pump simulation by one time step."""
        pass