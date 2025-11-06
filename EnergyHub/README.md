# Energy Hub

## Input Data

Meteorological input data, such as solar radiation and ambient air temperature, are obtained from [**Open-Meteo**](https://open-meteo.com/).  
All measurements are considered for **Cologne, Germany**.

For the PV modules, a **fixed panel tilt of 30°** and a **panel azimuth of 0° (south)** are assumed.  


| Variable         |  Unit      | Description                                 |
|------------------|------------|---------------------------------------------|
| temperature_2m   |   °C       | Air temperature at 2 meters above ground    |
| global_tilted_irradiance   |   W/m²       | Total radiation received on a tilted pane as average of the preceding hour. The calculation is assuming a fixed albedo of 20% and in isotropic sky. [...]   |

*Source: [Open-Meteo](https://open-meteo.com/)*


As a possible extension, [**PVLib**](https://pvlib-python.readthedocs.io/en/stable/) can be used to refine the PV performance modeling, allowing for more accurate calculations of irradiance, module temperature, and electrical output.

---

## Model

The **Energy Hub** model integrates photovoltaic generation, thermal storage, and energy conversion components.  
It provides a simulation environment for testing control strategies, including **Model Predictive Control (MPC)** and **PID-based control**.

---

### Heat Pump

#### Simplified Model
The heat pump is represented by a simplified model:

$\text{COP} = 2.5 + 0.075\cdot T_\text{ambient}$

This linear approximation ensures that the COP equals 2.5 at 0 °C and 4.0 at 20 °C, capturing the main efficiency trend of an air-source heat pump without requiring a detailed thermodynamic simulation.

---

#### PID control
As an additional feature, the **inlet temperature** computed by the MPC serves as a reference for a **PID controller** regulating the operation of a heat pump.  

In this case, the heat pump is simulated using [TESPy](https://tespy.readthedocs.io/en/main/).  
It is possible to run a **coupled simulation**, where the MPC or PID controller provides control signals (e.g., inlet temperature setpoints) to the TESPy heat pump model, while TESPy returns the resulting thermal and electrical performance (e.g., heat output, COP, power consumption).  

This allows for a more realistic, physics-based interaction between the control layer and the thermodynamic system model.


---

## MPC

Two approaches are implemented:

1. **`do-mpc`-based implementation**  
   Uses the [do-mpc](https://www.do-mpc.com/) framework for rapid prototyping and simulation of MPC controllers.

2. **Custom CasADi implementation**  
   The second approach uses [CasADi](https://web.casadi.org/) to model the MPC manually, providing deeper insight into the optimization process and the underlying mathematical formulation.

---

