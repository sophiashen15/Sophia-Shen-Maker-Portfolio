def estimate_co2_emission(distance_km, duration_hours, fuel_efficiency_kmpl, remainder_minutes):
    # Convert distance to miles
    distance_miles = distance_km / 1.60934

    # Calculate total fuel consumed (in liters)
    fuel_consumed_liters = distance_km / fuel_efficiency_kmpl

    # Assume CO2 emissions of 2.3 kg per liter of gasoline
    co2_emission_kg = fuel_consumed_liters * 2.3

    # Convert duration to hours
    total_hours = duration_hours + remainder_minutes / 60.0  # adding 48 minutes

    # Calculate CO2 emission rate (kg per hour)
    co2_emission_rate_kg_per_hour = co2_emission_kg / total_hours

    return co2_emission_kg, co2_emission_rate_kg_per_hour

# Truck only calculation
distance_traveled_km = 23.30
total_duration_hours = 6.0
extra_minutes = 52.0
fuel_efficiency_assumption = 10.0  # Assume 10 km per liter

co2_total, co2_rate = estimate_co2_emission(distance_traveled_km, total_duration_hours, fuel_efficiency_assumption, extra_minutes)

print("--------------------- TRUCK ONLY ---------------------")
print(f"Estimated total CO2 emissions: {co2_total:.2f} kg")
print(f"Estimated CO2 emission rate: {co2_rate:.2f} kg per hour")
print()

# Aeromile calculation
distance_traveled_km = 18.5
total_duration_hours = 5.0
extra_minutes = 18.0
fuel_efficiency_assumption = 10.0  # Assume 10 km per liter

co2_total, co2_rate = estimate_co2_emission(distance_traveled_km, total_duration_hours, fuel_efficiency_assumption, extra_minutes)


print("--------------------- AEROMILE ---------------------")
print(f"Estimated total CO2 emissions: {co2_total:.2f} kg")
print(f"Estimated CO2 emission rate: {co2_rate:.2f} kg per hour")
