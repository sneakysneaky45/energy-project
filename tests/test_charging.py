from datetime import datetime
import charging

def test_find_cheapest_charging_window():
    prices_ct_per_kwh = [25, 1, 25, 8, 8, 8]
    charging_power_kw = 11
    required_energy_kwh = 8.25

    first_slot_start = datetime(2026, 11, 13, 18, 0)

    result = charging.find_cheapest_charging_window(prices_ct_per_kwh, charging_power_kw, required_energy_kwh, first_slot_start)

    assert result.start == datetime(2026, 11, 13, 18, 45)
    assert result.end == datetime(2026, 11, 13, 19, 30)
    assert result.cost_ct == 66

def test_charges_only_remaining_energy_in_last_slot(): 
    prices_ct_per_kwh = [25, 1, 25, 8, 8, 8]
    charging_power_kw = 11
    required_energy_kwh = 3

    first_slot_start = datetime(2026, 11, 13, 18, 0)

    result = charging.find_cheapest_charging_window(prices_ct_per_kwh, charging_power_kw, required_energy_kwh, first_slot_start)

    assert result.start == datetime(2026, 11, 13, 18, 15)
    assert result.end == datetime(2026, 11, 13, 18, 31, 21, 818182)
    assert result.cost_ct == 9
