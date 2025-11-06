from typing import Any, Dict
from heat_pump.hp_base import HeatPumpBase

class TesPyHeatPump(HeatPumpBase):
    """Concrete implementation of a heat pump using TESPy library."""

    def __init__(self, model_params: Dict[str, Any]) -> None:
        """Initialize the TESPy heat pump with specific model parameters.

        Args:
            model_params: A dictionary containing parameters for the TESPy model.
        """
        super().__init__(name="TESPy Heat Pump")
        self.model_params = model_params
        self.mode = 'off'


    def get_status(self) -> Dict[str, Any]:
        """Retrieve the current status of the heat pump.

        Returns:
            A dictionary containing status information.
        """
        return {
            'mode': self.mode,
            'target_temperature': self.target_temperature,
            'model_params': self.model_params
        }
    

    def set_status(self, ambient_temperature: float, target_temperature: float) -> None:
        self.target_temperature = target_temperature


    def step(self) -> None:
        """Advance the heat pump simulation by one time step."""
        if self.mode == 'heating':
            print(f"Heating to {self.target_temperature}°C using TESPy model with params {self.model_params}.")
        elif self.mode == 'cooling':
            print(f"Cooling to {self.target_temperature}°C using TESPy model with params {self.model_params}.")
        else:
            print("TESPy heat pump is off.")