from pv.pv_base import PVBase
import pandas as pd

class OpenMeteoPV(PVBase):
    def __init__(self, data_path: str, Area: float = 50.0, eta: float = 0.95):
        super().__init__(name="OpenMeteo Photovoltaic System", Area=Area, eta=eta)

        # Load irradiance data
        self.df_irradiance = pd.read_csv(data_path)  


    def calculate_output(self, t: int) -> float:
        print(f"Calculating PV output at time {t} using OpenMeteo Data.")
        irradiance = self.df_irradiance.iloc[t]["global_tilted_irradiance"]
        power_output = self.Area * self.eta * irradiance / 1000.0  # kW
        return power_output

