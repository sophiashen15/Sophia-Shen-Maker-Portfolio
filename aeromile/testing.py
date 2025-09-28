order_of_stops = ['AD', 'AF', 'AG', 'BA', 'BE', 'BG', 'BP', 'BT', 'BY', 'BZ', 'CA', 'CG', 'CK', 'CM', 'CO', 'CP', 'CW',
                  'DJ', 'DL', 'DN', 'DQ', 'EC', 'EH', 'EO', 'EX', 'EY', 'FF', 'FH', 'FY', 'GB', 'GN', 'GP', 'GS', 'GU',
                  'GW', 'HB', 'HG', 'HN', 'HO', 'HR', 'HT', 'HW', 'IA', 'IJ', 'IM', 'IP', 'IW', 'JH', 'JM', 'KA', 'KG',
                  'KJ', 'KM', 'KN', 'KP', 'KU', 'LB', 'LD', 'LG', 'LK', 'LY', 'MA', 'MO', 'MQ', 'MR', 'MW', 'NE', 'NL',
                  'NM', 'NR', 'NU', 'PB', 'PJ', 'PS', 'PT', 'PX', 'QE', 'QM', 'QO', 'QX', 'RA', 'RG', 'RY', 'SC', 'SD',
                  'SF', 'SI', 'SQ', 'TC', 'TG', 'TH', 'TK', 'TQ', 'TY', 'UI', 'UJ', 'UN', 'UR', 'US', 'UU', 'UW', 'VA',
                  'VC', 'VW', 'WJ', 'WS', 'XB', 'XD', 'YE', 'YH', 'YJ', 'YN', 'YR', 'YY', 'ZB', 'ZE', 'ZP', 'ZU']

lst = ['QM', 'BY', 'VW', 'JH', 'LB', 'DL', 'GU', 'NR', 'SC', 'IJ', 'XB', 'KP', 'IW', 'TH', 'MR', 'CG', 'LG', 'DJ', 'UR', 'ZE', 'VA', 'BA', 'YH', 'CP', 'UJ', 'UW', 'HN', 'KJ', 'GN', 'TC', 'NE', 'LD', 'AF', 'KA', 'BT', 'UI', 'BG', 'CO', 'KG', 'EO', 'IA', 'YE', 'BZ', 'ZU', 'GS', 'NU', 'BP', 'IM', 'EY', 'MQ', 'US', 'PJ', 'GW', 'RY', 'FY', 'NM', 'HO', 'PS', 'LY', 'LK', 'QE', 'CK', 'HG', 'YN', 'JM', 'HW', 'IP', 'SI', 'CM', 'HB', 'SQ', 'ZP', 'EX', 'EC', 'BE', 'PB', 'HR', 'ZB', 'WJ', 'YY', 'QX'] + ['TG', 'GP', 'HT', 'AG', 'SF', 'CW', 'FH', 'TK', 'PT', 'KN', 'NL', 'DQ', 'DN', 'CA', 'MW', 'KM', 'RG', 'VC', 'KU', 'MA', 'RA', 'YR', 'WS', 'GB', 'FF', 'MO', 'TQ', 'XD', 'EH', 'YJ', 'TY', 'AD', 'QO', 'UN', 'UU', 'SD', 'PX']

# Find values that are in order_of_stops but not in lst
difference1 = list(set(order_of_stops) - set(lst))

# Find values that are in lst but not in order_of_stops
difference2 = list(set(lst) - set(order_of_stops))

# Combine the differences into a single list
all_differences = difference1 + difference2

print("Values different in order_of_stops:", difference1)
print("Values different in lst:", difference2)
print("All different values:", all_differences)
