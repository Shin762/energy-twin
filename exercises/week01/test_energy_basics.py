from energy_basics import (
    battery_soc_after,
    daily_energy,
    is_demand_over,
    kw_to_kwh,
    peak_cut,
    peak_hour,
)


def test_q1_kw_to_kwh():
    assert kw_to_kwh(100, 2) == 200
    assert kw_to_kwh(50, 0.5) == 25


def test_q2_is_demand_over():
    assert is_demand_over(510, 500) is True
    assert is_demand_over(500, 500) is False
    assert is_demand_over(480, 500) is False


def test_q3_daily_energy():
    assert daily_energy([10, 20, 30]) == 60
    assert daily_energy([]) == 0


def test_q4_peak_hour():
    assert peak_hour([10, 50, 30, 50]) == 1
    assert peak_hour([5]) == 0


def test_q5_battery_soc_after():
    assert battery_soc_after(50, 20, 1, 100) == 70
    assert battery_soc_after(90, 20, 1, 100) == 100
    assert battery_soc_after(10, -30, 1, 100) == 0
    assert battery_soc_after(50, -10, 2, 100) == 30


def test_q6_peak_cut():
    assert peak_cut([400, 520, 480, 600], 500) == [0, 20, 0, 100]
    assert peak_cut([], 500) == []
