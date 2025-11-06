import os
import sys
import argparse
import logging
import signal
from datetime import datetime
from pathlib import Path
from typing import Dict, Any
import yaml

from core.factory import build_component
from core.registry import HeatPumpRegistry as HP_REGISTRY
from core.registry import PVRegistry as PV_REGISTRY


# ---------- CLI ----------
def parse_args():
    p = argparse.ArgumentParser(description="Energy Hub - Simulation runner")
    p.add_argument("--config", default="config.yaml", help="Path to YAML config")
    p.add_argument("--hp", help="Override heat pump type (simple/tespy/off)")
    p.add_argument("--pv", help="Override pv type (pvlib/dummy/off)")
    p.add_argument("--horizon", type=int, help="Override run horizon")
    p.add_argument("--log", dest="log_level", choices=["DEBUG", "INFO", "WARNING", "ERROR"])
    p.add_argument("--outdir", help="Where to store run artifacts (logs, config, results)")
    return p.parse_args()


# ---------- Config I/O ----------
def load_yaml(path: str) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}

def env_override(cfg: dict) -> None:
    # Beispiel: HP_TYPE=tespy überschreibt components.heat_pump.type
    hp_type = os.getenv("HP_TYPE")
    pv_type = os.getenv("PV_TYPE")
    if hp_type:
        cfg["components"]["heat_pump"]["type"] = hp_type
    if pv_type:
        cfg["components"]["pv"]["type"] = pv_type



def apply_cli_overrides(cfg: dict, args) -> None:
    if args.hp: cfg["components"]["heat_pump"]["type"] = args.hp
    if args.pv: cfg["components"]["pv"]["type"] = args.pv
    if args.horizon is not None: cfg["run"]["horizon"] = args.horizon
    if args.log_level: cfg["run"]["log_level"] = args.log_level

def setup_logging(level: str):
    logging.basicConfig(level=getattr(logging, level, logging.INFO),
                        format="%(asctime)s | %(levelname)s | %(message)s")
    
    
def make_outdir(user_outdir: str | None) -> Path:
    if user_outdir:
        outdir = Path(user_outdir)
    else:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        outdir = Path("runs") / stamp
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir




# ---------- Entry ----------
def main():
    args = parse_args()
    cfg = load_yaml(args.config)

    
    setup_logging(cfg["run"]["log_level"])

    hp_cfg = cfg["components"]["heat_pump"]
    pv_cfg = cfg["components"]["pv"]

    hp = build_component(hp_cfg["type"], hp_cfg.get("params"), HP_REGISTRY)
    pv = build_component(pv_cfg["type"], pv_cfg.get("params"), PV_REGISTRY)
   
   

    #logging.info({"t": t, "hp": res_hp, "p_pv": p_pv})




if __name__ == "__main__":
    main()