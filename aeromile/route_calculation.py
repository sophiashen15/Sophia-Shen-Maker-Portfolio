import json
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime, timedelta
import mplcursors


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


# Specify the path to your JSON file
json_file_path = 'sample_route_data.json'

# Open the JSON file and load its contents
with open(json_file_path, 'r') as json_file:
    # Load JSON data
    data = json.load(json_file)

data = data["RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77"]["stops"]
for stop in data.keys():
    if data[stop]['stop_number'] == 1:
        data.pop(stop)
        break
print(data)

# Extract latitude and longitude for each stop and sort them based on "stop_number"
order_of_stops = sorted(data.values(), key=lambda x: x["stop_number"])
latitudes = [stop["lat"] for stop in order_of_stops]
longitudes = [stop["lng"] for stop in order_of_stops]

# Plot the points on a scatter plot with different colors
scat = plt.scatter(longitudes, latitudes, label="Dropoff Points", color='green', marker='o', s=100)  # Different color for dropoff points
mplcursors.cursor(scat, hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Stop: {order_of_stops[sel.target.index]}"))


# Connect the points to trace the path
plt.plot(longitudes, latitudes, linestyle='-', color='blue', marker='o', markersize=5, label='Path')  # Different color for path

# Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Dropoff Points and Path")
plt.legend()
plt.grid(True)
plt.show()

# Calculate the total distance traveled along the path
total_distance = 0
for i in range(len(order_of_stops) - 1):
    lat1, lon1 = order_of_stops[i]["lat"], order_of_stops[i]["lng"]
    lat2, lon2 = order_of_stops[i + 1]["lat"], order_of_stops[i + 1]["lng"]
    total_distance += (haversine_distance(lat1, lon1, lat2, lon2) * 1.31)  # distance = haversine distance * route network for LA

print(f"Total distance traveled along the path: {total_distance:.2f} kilometers")

def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles

miles_result = km_to_miles(total_distance)
print(f"Total distance traveled along the path: {miles_result:.2f} miles")

# Extract stops
stops = data

# Count the number of stops visited
num_stops_visited = len(stops)

print(f"The number of stops visited is: {num_stops_visited}")

# Extract latitude and longitude for each stop and sort them based on "stop_number"
order_of_stops = sorted(stops.values(), key=lambda x: x["stop_number"])

# Create a list to store the order of stop names
order_of_stop_names = [stop_name for stop_name in stops]
print(order_of_stop_names)
