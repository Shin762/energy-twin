from pathlib import Path

import pytest

from energy_structures import (
    Battery,
    Generator,
    count_by_status,
    energy_by_unit,
    read_demand_csv,
    simulate_peak_cut,
)

DATA_DIR = Path(__file__).parent / "data"


def test_q1_count_by_status():
    records = [
        {"unit": "CGS1", "status": "run"},
        {"unit": "CGS2", "status": "stop"},
        {"unit": "CGS3", "status": "run"},
    ]
    assert count_by_status(records) == {"run": 2, "stop": 1}
    assert count_by_status([]) == {}


def test_q2_energy_by_unit():
    records = [
        {"unit": "CGS1", "kwh": 100},
        {"unit": "CGS2", "kwh": 50},
        {"unit": "CGS1", "kwh": 30},
    ]
    assert energy_by_unit(records) == {"CGS1": 130, "CGS2": 50}
    assert energy_by_unit([]) == {}


def test_q3_battery():
    b = Battery(100, 50)
    assert b.capacity_kwh == 100
    assert b.charge(30) == 30
    assert b.soc_kwh == 80
    assert b.charge(30) == 20
    assert b.soc_kwh == 100
    assert b.discharge(130) == 100
    assert b.soc_kwh == 0
    assert Battery(200, 50).soc_ratio() == 0.25
    assert Battery(100).soc_kwh == 0


def test_q4_generator():
    g = Generator(100, 0.4)
    assert g.fuel_input_kw(40) == pytest.approx(100)
    assert g.fuel_input_kw(0) == 0
    with pytest.raises(ValueError):
        g.fuel_input_kw(120)
    with pytest.raises(ValueError):
        g.fuel_input_kw(-1)


def test_q5_read_demand_csv():
    values = read_demand_csv(DATA_DIR / "demand_sample.csv")
    assert values == [320.5, 310.0, 305.2, 450.0, 520.8, 498.3]
    assert all(isinstance(v, float) for v in values)


def test_q6_simulate_peak_cut():
    battery = Battery(100, 50)
    result = simulate_peak_cut([400, 520, 480, 600, 550], 500, battery)
    assert result == [400, 500, 480, 570, 550]
    assert battery.soc_kwh == 0
