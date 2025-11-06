from typing import Any, Dict
from heat_pump.hp_base import HeatPumpBase

class HeatPump(HeatPumpBase):
    """Implementation of a heat pump for general use. 
        Does not rely on any specific simulation library, but rather implements a simple model used for easy calculations."""

    def __init__(self, offset: float = 2.5, alpha: float = 0.075) -> None:
        """Initialize the heat pump.

        Args:
            offset: The temperature offset for the heat pump.
        """
        super().__init__(name="Heat Pump Simplified Model")
        self.offset = offset
        self.alpha = alpha
        self.cop = 3.5                  # Default Coefficient of Performance

    def set_status(self, ambient_temperature: float, target_temperature: float) -> None:
        """Set the operational status of the heat pump.

        Args:
            ambient_temperature: The ambient temperature in Celsius.
            target_temperature: The desired target temperature in Celsius.
        """

        # Linear COP approximation
        self.cop = min(4.0, max(1.0, self.alpha * ambient_temperature + self.offset)) 
        self.target_temperature = target_temperature


    def get_status(self) -> Dict[str, Any]:
        """Retrieve the current status of the heat pump.

        Returns:
            A dictionary containing status information.
        """
        return {
            'cop': self.cop,
            'target_temperature': self.target_temperature
        }

    def step(self) -> None:
        """Advance the heat pump simulation by one time step."""
        print(f"Heat pump operating with COP: {self.cop} to reach target temperature: {self.target_temperature}°C.")
        # Simulate the heat pump's operation (this is a placeholder for actual logic)