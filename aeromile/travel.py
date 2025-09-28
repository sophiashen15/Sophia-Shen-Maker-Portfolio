import json

# Load data from the JSON file
with open('sample_travel_times.json', 'r') as file:
    travel_times_data = json.load(file)

full_dict = travel_times_data['RouteID_00143bdd-0a6b-49ec-bb35-36593d303e77']

def calculate_time(current, next_stop):
    stop_dict = full_dict[current]
    time = stop_dict[next_stop]
    return time

# Define the order of stops
order_of_stops = ['AD', 'AF', 'AG', 'BA', 'BE', 'BG', 'BP', 'BT', 'BY', 'BZ', 'CA', 'CG', 'CK', 'CM', 'CO', 'CP', 'CW',
                  'DJ', 'DL', 'DN', 'DQ', 'EC', 'EH', 'EO', 'EX', 'EY', 'FF', 'FH', 'FY', 'GB', 'GN', 'GP', 'GS', 'GU',
                  'GW', 'HB', 'HG', 'HN', 'HO', 'HR', 'HT', 'HW', 'IA', 'IJ', 'IM', 'IP', 'IW', 'JH', 'JM', 'KA', 'KG',
                  'KJ', 'KM', 'KN', 'KP', 'KU', 'LB', 'LD', 'LG', 'LK', 'LY', 'MA', 'MO', 'MQ', 'MR', 'MW', 'NE', 'NL',
                  'NM', 'NR', 'NU', 'PB', 'PJ', 'PS', 'PT', 'PX', 'QE', 'QM', 'QO', 'QX', 'RA', 'RG', 'RY', 'SC', 'SD',
                  'SF', 'SI', 'SQ', 'TC', 'TG', 'TH', 'TK', 'TQ', 'TY', 'UI', 'UJ', 'UN', 'UR', 'US', 'UU', 'UW', 'VA',
                  'VC', 'VW', 'WJ', 'WS', 'XB', 'XD', 'YE', 'YH', 'YJ', 'YN', 'YR', 'YY', 'ZB', 'ZE', 'ZP', 'ZU']

total_time = 0
for i in range(len(order_of_stops) - 1):
    total_time += calculate_time(order_of_stops[i], order_of_stops[i+1])

# Function to convert seconds to hours and minutes
def convert_seconds_to_hours_minutes(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return hours, minutes


total_hours, total_minutes = convert_seconds_to_hours_minutes(total_time)
print(f"\nTotal Time for All Stops: {total_hours} hours and {total_minutes} minutes")

