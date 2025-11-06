from abc import ABC, abstractmethod
from typing import Any, Dict

class PVBase(ABC):
    """Abstract base class for photovoltaic (PV) system implementations."""

    def __init__(self, name: str = "Photovoltaic System", Area: float = 50.0, eta: float = 0.95):
        self.name = name
        self.Area = Area
        self.eta = eta
        print(f"{self.name} initialized.")


    @abstractmethod
    def calculate_output(self, t: int) -> float:
        """Calculate the power output of the PV system at time t.

        Args:
            t: The current time step.

        Returns:
            The power output in kW.
        """
        pass