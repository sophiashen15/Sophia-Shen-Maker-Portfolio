import json
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta

# Specify the path to your JSON file
json_file_path = 'sample_package_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    data = json.load(json_file)

# Function to calculate total time for each stop
def calculate_total_time(route_data):
    total_time_per_stop = {}
    total_time_all_stops = 0
    for stop, packages in route_data.items():
        total_time = sum(package_data["planned_service_time_seconds"] for package_data in packages.values())
        total_time_per_stop[stop] = total_time
        total_time_all_stops += total_time
    return total_time_per_stop, total_time_all_stops

# Function to convert seconds to hours and minutes
def convert_seconds_to_hours_minutes(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return hours, minutes

# Calculate total time for each stop and total time for all stops
total_time_per_stop, total_time_all_stops = calculate_total_time(data["RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77"])

# Print the result
for stop, total_time in total_time_per_stop.items():
    print(f"Stop {stop}: Total Time - {total_time} seconds")

total_hours, total_minutes = convert_seconds_to_hours_minutes(total_time_all_stops)
print(f"\nTotal Time for All Stops: {total_hours} hours and {total_minutes} minutes")
