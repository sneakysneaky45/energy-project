from dataclasses import dataclass
from datetime import datetime, timedelta
from math import ceil


@dataclass
class ChargingWindow:
	start: datetime
	end: datetime
	cost_ct: float

def find_cheapest_charging_window(prices_ct_per_kwh, charging_power_kw, required_energy_kwh, first_slot_start):
    costs_per_start_time= {}

    required_charging_time_hours = required_energy_kwh/charging_power_kw
    slot_count = ceil(required_charging_time_hours/0.25)

    if (len(prices_ct_per_kwh) < slot_count): 
          raise ValueError("Not enough price intervals!")
    charged_per_15mins = charging_power_kw/4
    energy_last_slot = required_energy_kwh - (slot_count-1)*charged_per_15mins
    for startPrice in range(len(prices_ct_per_kwh)-slot_count+1):
          current_sum = sum(
                price * charged_per_15mins
                for price in prices_ct_per_kwh[startPrice : startPrice + slot_count-1]
                 
          )
          last_slot_price = prices_ct_per_kwh[startPrice + slot_count-1]
          current_sum += last_slot_price * energy_last_slot
          costs_per_start_time[startPrice] = current_sum

    best_start_index = min(costs_per_start_time, key=costs_per_start_time.get)
    start = first_slot_start + timedelta(minutes=15 * best_start_index)
    end = start + timedelta(hours= required_charging_time_hours)
    return ChargingWindow(start=start, end=end, cost_ct=costs_per_start_time[best_start_index])
