# Routing Algorithm Code
# Written by: Sophia Shen
# --------------------------------------------------------------------------------------

# Import neccessary libraries
import numpy as np
import scipy.stats as stats
import json
import random
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
import math


# Specify the path to your JSON file
json_file_path = 'sample_package_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    pkg_data = json.load(json_file)

data = pkg_data['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77'] # focus on one route
for stop in data.keys():
    if stop == 'VE':
        data.pop(stop)
        break
# --------------------------------------------------------------------------------------

# Write function to estimate package weight based on volume
# Assumptions: 86% of packages are below 5 lbs, package weight follows a normal distribution

def estimate_package_weight(volume_cm3):
    # Desired percentage below 5 lbs (adjust as needed)
    target_percentage_below_5lbs = 0.86

    # Assuming standard deviation for weight distribution
    weight_std_dev = 1.0

    # Calculate the Z-score corresponding to the desired percentage
    z_score = stats.norm.ppf(target_percentage_below_5lbs)

    # Calculate the adjusted mean weight
    mean_weight = 5 - z_score * weight_std_dev

    # Generate a random weight from a normal distribution
    estimated_weight = max(0, random.normalvariate(mean_weight, weight_std_dev))

    return estimated_weight

# --------------------------------------------------------------------------------------

# Create new dictionary that has the estimated weights

new_data = {}

# Estimate weights for all the packages
for key in data.keys():  # loop thru the stops
    packages = data[key]  # get packages for each stop
    mini_dict = {}
    for package in packages.keys():  # loop thru packages
        dimensions = packages[package]['dimensions']  # calculate volume of each package
        volume = dimensions['depth_cm'] * dimensions['height_cm'] * dimensions['width_cm']
        mini_dict[package] = estimate_package_weight(volume)  # add to mini_dict for new_data
    new_data[key] = mini_dict

# --------------------------------------------------------------------------------------

# Separate packages into "Small" and "Big" sets
def is_big(weight):
    return (weight > 3)

def is_small(weight):
    return (weight <= 3)

small_packages = {}
big_packages = {}

for stop in new_data.keys():
    package_lst = new_data[stop]
    for package in package_lst.keys():
        if is_small(package_lst[package]):
            if stop not in small_packages.keys():
                small_packages[stop] = {}
                small_packages[stop][package] = package_lst[package]
            else:
                small_packages[stop][package] = package_lst[package]
        if is_big(package_lst[package]):
            if stop not in big_packages.keys():
                big_packages[stop] = {}
                big_packages[stop][package] = package_lst[package]
            else:
                big_packages[stop][package] = package_lst[package]


all_nonempty_stops = ['BE', 'BT', 'CA', 'CG', 'CP', 'DJ', 'EH', 'EY', 'FH', 'GB', 'GS', 'HB', 'HO', 'HR', 'HW', 'IA', 'IW', 'KA', 'KG', 'KJ', 'KN', 'LD', 'MA', 'MO', 'MW', 'NL', 'PB', 'PS', 'PX', 'QX', 'SD', 'TG', 'TH', 'TQ', 'UI', 'UN', 'UW', 'XB', 'YJ', 'YR', 'YY'] + ['AD', 'AG', 'BA', 'BE', 'BG', 'BP', 'BT', 'BY', 'BZ', 'CA', 'CG', 'CM', 'CO', 'CP', 'CW', 'DJ', 'DL', 'DN', 'DQ', 'EC', 'EH', 'EO', 'EX', 'FF', 'FH', 'FY', 'GB', 'GP', 'GS', 'GU', 'GW', 'HB', 'HG', 'HN', 'HO', 'HR', 'HT', 'HW', 'IA', 'IJ', 'IM', 'IP', 'IW', 'JH', 'JM', 'KA', 'KG', 'KJ', 'KM', 'KN', 'KP', 'LB', 'LG', 'LY', 'MA', 'MO', 'MQ', 'MR', 'MW', 'NE', 'NL', 'NM', 'NR', 'NU', 'PB', 'PJ', 'PS', 'PT', 'PX', 'QE', 'QM', 'QO', 'QX', 'RA', 'RG', 'RY', 'SC', 'SD', 'SF', 'SI', 'SQ', 'TC', 'TG', 'TH', 'TK', 'TQ', 'TY', 'UI', 'UJ', 'UN', 'UR', 'US', 'UU', 'UW', 'VA', 'VC', 'VW', 'WJ', 'WS', 'XB', 'YE', 'YH', 'YJ', 'YN', 'YR', 'YY', 'ZB', 'ZE', 'ZP', 'ZU']

# Count the number of packages and stops in dataset
pkg_count = 0
stop_count = 0
for stop in new_data.keys():
    stop_count += 1
    package_lst = new_data[stop]
    for package in package_lst.keys():
        pkg_count += 1

# print("Stops: " + str(stop_count))
# print("Num pkgs: " + str(pkg_count))

# --------------------------------------------------------------------------------------

# Import in the route data
json_file_path = 'sample_route_data.json'
route_data = json.load(open(json_file_path))
route_data = route_data['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77']  # focus on one route
stops = route_data['stops']

# Combine route data with package weight data
for stop in stops.keys():
    if stop in small_packages.keys():
        small_dict = stops[stop]
        pkgs = small_packages[stop]
        small_dict["Packages"] = pkgs  # add packages as key with dictionary of packages as value
        stops[stop] = small_dict
    elif stop in big_packages.keys():
        small_dict = stops[stop]
        pkgs = big_packages[stop]
        small_dict["Packages"] = pkgs  # add packages as key with dictionary of packages as value
        stops[stop] = small_dict


# ------------------------ HELPER FUNCTIONS ------------------------

# For any given stop, check if all packages are <= 3 lbs
def check_all_small(stop):
    if "Packages" in stops[stop]:
        pkgs = stops[stop]['Packages']
        all_small = True
        for package in pkgs.keys():
            if pkgs[package] > 3:
                all_small = False
        return all_small


# For any given stop, check if any package is > 3 lbs
def check_if_any_big(stop):
    if "Packages" in stops[stop]:
        pkgs = stops[stop]["Packages"]
        any_big = True
        for package in pkgs.keys():
            if pkgs[package] <= 3:
                any_big = False
        return any_big

# Find the next stop based on dropoff number
def find_next_stop(stop):
    prev_num = stops[stop]["stop_number"]
    for stop in stops.keys():
        if stops[stop]["stop_number"] == prev_num + 1:
            return stop

# For any dictionary
def get_key_from_value(dictionary, target_value):
    for key, value in dictionary.items():
        if value == target_value:
            return key
    return None  # Return None if the value is not found

# Find the distance between two stops given their latitude and longitude
def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate distance
    distance = R * c
    return distance

# ------------------------ end of helpers ------------------------

# Find the starting stop (its VE)
starting_stop = ''
for stop in stops.keys():
    if stops[stop]['stop_number'] == 1:
        starting_stop = stop
        break

# Sort the stops into human delivery and drone delivery

human_stop = {}
drone_stop = {}

for stop in stops.keys():
    if check_if_any_big(stop):
        human_stop[stop] = stops[stop]
    elif check_all_small(stop):
        drone_stop[stop] = stops[stop]

human_stop_str = ", ".join(map(str, human_stop))
drone_stop_str = ", ".join(map(str, drone_stop))

# print("Human delivery: " + human_stop_str)
# print("Drone delivery: " + drone_stop_str)

# --------------------------------------------------------------------------------------

# Visualize original path with a hover function!

import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors for hover function

# Specify the path to your JSON file
json_file_path = 'sample_route_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    data = json.load(json_file)

# Extract latitude and longitude for each stop and sort them based on "stop_number"
order_of_stops = sorted(data["RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77"]["stops"].values(), key=lambda x: x["stop_number"])
latitudes = [stop["lat"] for stop in order_of_stops]
longitudes = [stop["lng"] for stop in order_of_stops]

# Separate stops into human_stop and drone_stop
human_stop_latitudes = [human_stop[stop]["lat"] for stop in human_stop.keys()]
human_stop_longitudes = [human_stop[stop]["lng"] for stop in human_stop.keys()]

drone_stop_latitudes = [drone_stop[stop]["lat"] for stop in drone_stop.keys()]
drone_stop_longitudes = [drone_stop[stop]["lng"] for stop in drone_stop.keys()]

human_scatter = plt.scatter(human_stop_longitudes, human_stop_latitudes, label="Human Points", color='green', marker='o', s=100)
human_names = [[stop, human_stop[stop]["stop_number"], len(human_stop[stop]["Packages"])] for stop in human_stop.keys()]
mplcursors.cursor(human_scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Human Stop: {human_names[sel.target.index]}"))

# Scatter plot for drone stops with hover text
drone_scatter = plt.scatter(drone_stop_longitudes, drone_stop_latitudes, label="Drone Stops", color='blue', marker='o', s=100)
drone_names = [[stop, drone_stop[stop]["stop_number"], len(drone_stop[stop]["Packages"])] for stop in drone_stop.keys()]
mplcursors.cursor(drone_scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Drone Stop: {drone_names[sel.target.index]}"))

plt.plot(longitudes, latitudes, linestyle='-', color='black', marker='o', markersize=5, label='TRUCK ONLY Path')  # Different color for path

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Human and Drone Delivery Points with TRUCK ONLY Path")
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------------------------------------------------------------

# Implement the algorithm!!

# GENERAL ALGORITHM EXPLANATION: for each drone stop, check its distance from the three human stops before it and the three human stops after it. 
# the drone stop will choose to take off at the closest human stop. 

combined_stops = {}


# Create 2 dictionaries where the key is the stop name and the value is the stop_number
human_stop_nums = {}
for stop in human_stop.keys():
    human_stop_nums[stop] = human_stop[stop]["stop_number"]

drone_stop_nums = {}
for stop in drone_stop.keys():
    drone_stop_nums[stop] = drone_stop[stop]["stop_number"]


for stop in drone_stop.keys():
    stop_num = drone_stop_nums[stop]
    prev_and_next_3 = {}
    for i in range(1, 4):
        h_prev_stop = get_key_from_value(human_stop_nums, stop_num - i)
        h_next_stop = get_key_from_value(human_stop_nums, stop_num + i) # potential problem, one of the values is None since its a drone stop
        if h_prev_stop is not None:
            prev_and_next_3[h_prev_stop] = stops[h_prev_stop]
        if h_next_stop is not None:
            prev_and_next_3[h_next_stop] = stops[h_next_stop]

    smallest_distance = float('inf')
    optimal_stop = None
    lat1, lon1 = drone_stop[stop]['lat'], drone_stop[stop]['lng']

    # Compare the distances from the drone stop and select the optimal point
    for key in prev_and_next_3.keys():
        lat2, lon2 = prev_and_next_3[key]['lat'], prev_and_next_3[key]['lng']
        distance = haversine_distance(lat1, lon1, lat2, lon2) * 1.31  # distance = haversine distance * route network for LA
        if distance < smallest_distance: 
            smallest_distance = distance
            optimal_stop = key

    if optimal_stop in combined_stops.keys():
        combined_stops[optimal_stop][stop] = smallest_distance
    else:
        combined_stops[optimal_stop] = {}
        combined_stops[optimal_stop][stop] = smallest_distance


# --------------------------------------------------------------------------------------
# Visualize NEW path with a hover function!

# Specify the path to your JSON file
json_file_path = 'sample_route_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    data = json.load(json_file)

# Extract latitude and longitude for each stop and sort them based on "stop_number"
order_of_stops = sorted(data["RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77"]["stops"].values(), key=lambda x: x["stop_number"])
latitudes = [stop["lat"] for stop in order_of_stops]
longitudes = [stop["lng"] for stop in order_of_stops]

# Separate stops into human_stop and drone_stop
order_of_human_stops = sorted(human_stop.values(), key=lambda x: x["stop_number"])
human_stop_latitudes = [stop["lat"] for stop in order_of_human_stops]
human_stop_longitudes = [stop["lng"] for stop in order_of_human_stops]

order_of_drone_stops = sorted(drone_stop.values(), key=lambda x: x["stop_number"])
drone_stop_latitudes = [stop["lat"] for stop in order_of_drone_stops]
drone_stop_longitudes = [stop["lng"] for stop in order_of_drone_stops]

# Scatter plot for human stops with hover text
human_scatter = plt.scatter(human_stop_longitudes, human_stop_latitudes, label="Human Stops", color='green', marker='o', s=100)
human_names = {stop: {"name": stop, "number": human_stop[stop]["stop_number"], "packages": len(human_stop[stop]["Packages"])} for stop in human_stop.keys()}
#mplcursors.cursor(human_scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Human Stop: {human_names[sel.target.index]}"))


# Scatter plot for drone stops with hover text
drone_scatter = plt.scatter(drone_stop_longitudes, drone_stop_latitudes, label="Drone Stops", color='blue', marker='o', s=100)
drone_names = {stop: {"name": stop, "number": drone_stop[stop]["stop_number"], "packages": len(drone_stop[stop]["Packages"])} for stop in drone_stop.keys()}
#mplcursors.cursor(drone_scatter, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Drone Stop: {drone_names[sel.target.index]}"))

# Print debugging information
for h_stop in combined_stops.keys():
    if h_stop in stops:
        human_x = stops[h_stop]['lng']
        human_y = stops[h_stop]['lat']

        for d_stop in combined_stops[h_stop]:
            if d_stop in stops:
                drone_x = stops[d_stop]['lng']
                drone_y = stops[d_stop]['lat']

                # Plot the line
                plt.plot([human_x, drone_x], [human_y, drone_y], linestyle='--', color='black')

plt.plot(human_stop_longitudes, human_stop_latitudes, linestyle='-', color='black', marker='o', markersize=5, label='TRUCK+DRONE Path')  # Different color for path

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Human and Drone Delivery Points with TRUCK+DRONE Path")
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------------------------------------------------------------

# Calculate the new statistics for truck+drone delivery


def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

# ----------------------------------

# Calculate the total distance traveled along the human path
total_truck_distance = 0
for i in range(len(order_of_human_stops) - 1):
    lat1, lon1 = order_of_human_stops[i]["lat"], order_of_human_stops[i]["lng"]
    lat2, lon2 = order_of_human_stops[i + 1]["lat"], order_of_human_stops[i + 1]["lng"]
    total_truck_distance += (haversine_distance(lat1, lon1, lat2, lon2) * 1.31)  # distance = haversine distance * route network for LA


print(f"Total distance traveled along the truck path: {total_truck_distance:.2f} kilometers")
miles_result = km_to_miles(total_truck_distance)
print(f"Total distance traveled along the truck path: {miles_result:.2f} miles")

# ----------------------------------

# Calculate the total distance traveled by drone
total_drone_distance = 0
for value in combined_stops.values():
    for key in value.keys():
        total_drone_distance += value[key]

total_drone_distance *= 2 # since the drone has to fly to the address and back to the truck
print(f"Total distance traveled along the drone path: {total_drone_distance:.2f} kilometers")
miles_result = km_to_miles(total_drone_distance)
print(f"Total distance traveled along the drone path: {miles_result:.2f} miles")

# ----------------------------------

drone_stop_order = sorted(drone_stop.keys(), key=lambda stop: drone_stop[stop]['stop_number'])
# print(drone_stop_order)

h_stops = []
for stop in stops:
    if stop not in drone_stop_order:
        h_stops.append(stop)

# Load data from the JSON file
with open('sample_travel_times.json', 'r') as file:
    travel_times_data = json.load(file)

full_dict = travel_times_data['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77']

def calculate_time(current, next_stop):
    stop_dict = full_dict[current]
    time = stop_dict[next_stop]
    return time

total_time = 0
for i in range(len(h_stops) - 1):
    total_time += calculate_time(h_stops[i], h_stops[i+1])

# Function to convert seconds to hours and minutes
def convert_seconds_to_hours_minutes(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return hours, minutes

total_hours, total_minutes = convert_seconds_to_hours_minutes(total_time)
print(f"\nTotal Driving Time for All Truck Stops: {total_hours} hours and {total_minutes} minutes")

# ----------------------------------
# Calculate total time traveled by drone

def hours_to_minutes_and_hours(total_hours):
    # Check if total_hours is NaN
    if math.isnan(total_hours):
        print("Error: total_hours is NaN")
        # Handle NaN case, maybe return a default value or raise an exception
        return 0, 0
    
    # Rest of your code
    minutes = total_hours * 60
    
    # Check if minutes is NaN
    if math.isnan(minutes):
        print("Error: minutes is NaN")
        # Handle NaN case, maybe return a default value or raise an exception
        return 0, 0
    
    print("Debug: minutes =", minutes)
    
    remaining_hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)
    
    print("Debug: remaining_hours =", remaining_hours)
    print("Debug: remaining_minutes =", remaining_minutes)
    
    return remaining_minutes, remaining_hours

total_drone_hours = total_drone_distance * (1/30)  # time = distance * (time / distance)
mins, hours = hours_to_minutes_and_hours(total_drone_hours)
print(f"\nTotal Flying Time for All Drone Stops: {hours} hours and {mins} minutes")

# ----------------------------------
# Calculate total time for delivery by hand

# Specify the path to your JSON file
json_file_path = 'sample_package_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    data = json.load(json_file)

data = data['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77']

# Make a dictionary for data with ONLY the human stops
human_dictionary = {}
for h_stop in h_stops:
    human_dictionary[h_stop] = data[h_stop]


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
total_time_per_stop, total_time_all_stops = calculate_total_time(human_dictionary)

# Print the result
for stop, total_time in total_time_per_stop.items():
    print(f"Stop {stop}: Total Time - {total_time} seconds")

total_hours, total_minutes = convert_seconds_to_hours_minutes(total_time_all_stops)
print(f"\nTotal Time for All Stops: {total_hours} hours and {total_minutes} minutes")
