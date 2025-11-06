from heat_pump.cop_impl import HeatPump
from heat_pump.tespy_impl import TesPyHeatPump
from pv.pvlib_impl import PVLibPV
from pv.openmeteo_impl import OpenMeteoPV
from mpc.casadi_impl import CasadiMPC
from mpc.dompc_impl import DoMPC    

HeatPumpRegistry = {
    "simple": HeatPump,
    "tespy": TesPyHeatPump,
    "off": None,
}

PVRegistry = {
    "pvlib": PVLibPV,      
    "openMeteo": OpenMeteoPV, 
    "off": None,      
}

MPCRegistry = {
    "casadi": CasadiMPC,      
    "do-mpc": DoMPC, 
    "off": None,      
}


PIDRegistry = {
    "on": None,
    "off": None,
}