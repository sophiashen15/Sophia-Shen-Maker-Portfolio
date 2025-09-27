import matplotlib.pyplot as plt

# ------------------------------ REDUCTION BAR CHART ------------------------------ 


data = {
    'Vehicle Miles Traveled': 20.65,
    'Driving time': 22.82,
    'Delivery time': 43.90,
    'CO2 emissions': 20.71,
    'Total time': 20.10
}

categories = list(data.keys())
values = list(data.values())

plt.bar(categories, values, color='skyblue')
plt.xlabel('Categories')
plt.ylabel('Reduction Percentage (%)')
plt.title('Comparing Truck-only with Aeromile Model')
plt.ylim(0, max(values) + 5)

# Add percentage values on top of each bar
for i, v in enumerate(values):
    plt.text(i, v + 1, f'{v:.2f}%', ha='center', va='bottom')

plt.xticks(rotation=30, ha='right')
plt.show()


# ------------------------------ COMPARISION BAR CHART ------------------------------ 

import matplotlib.pyplot as plt
import numpy as np

# Data for truck only
truck_data = {
    'VMT': 14.48,
    'Driving time': round(6 + 52/60, 2),  # Convert hours and minutes to decimal hours
    'Delivery time': round(3 + 35/60, 2),  # Convert hours and minutes to decimal hours
    'CO2 emissions': round(5.36, 2)
}

# Data for Aeromile model
aeromile_data = {
    'VMT': round(11.49, 2),
    'Driving time': round(5 + 18/60, 2),  # Convert hours and minutes to decimal hours
    'Delivery time': round(1 + 55/60, 2),  # Convert hours and minutes to decimal hours
    'CO2 emissions': round(4.25, 2)
}

categories = list(truck_data.keys())
bar_width = 0.35  # Width of the bars

fig, ax = plt.subplots()

bar1 = ax.bar(np.arange(len(categories)) - bar_width/2, list(truck_data.values()), bar_width, label='Truck-only', color='skyblue')
bar2 = ax.bar(np.arange(len(categories)) + bar_width/2, list(aeromile_data.values()), bar_width, label='Aeromile', color='darkblue')

# Add actual values on top of the bars with units
for i, v in enumerate(list(truck_data.values())):
    if categories[i] == 'VMT':
        ax.text(i - bar_width/2, v + 0.1, f'{round(v, 2)} miles', ha='center', va='bottom', color='black')
    else:
        ax.text(i - bar_width/2, v + 0.1, f'{round(v, 2)} hours' if 'time' in categories[i] else f'{round(v, 2)} kg', ha='center', va='bottom', color='black')

for i, v in enumerate(list(aeromile_data.values())):
    if categories[i] == 'VMT':
        ax.text(i + bar_width/2, v + 0.1, f'{round(v, 2)} miles', ha='center', va='bottom', color='black')
    else:
        ax.text(i + bar_width/2, v + 0.1, f'{round(v, 2)} hours' if 'time' in categories[i] else f'{round(v, 2)} kg', ha='center', va='bottom', color='black')

ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Comparison of truck-only model and Aeromile model')
ax.set_xticks(np.arange(len(categories)))  # Set x-tick positions to the center of each pair of bars
ax.set_xticklabels(categories)  # Set x-tick labels

ax.legend()

plt.show()



