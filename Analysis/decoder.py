import json

# Read data from the file
with open('data.txt', 'r') as file:
    data = file.readlines()

# Initialize a dictionary to store the average RSSI for each location and receiver
average_rssi = {}

# Process each line of data
for line in data:
    record = json.loads(line.strip())  # Parse JSON string to dictionary
    receiver = record['RCV']
    location = record['Location']

    # Initialize a list to store RSSI values for each receiver at the location
    if location not in average_rssi:
        average_rssi[location] = {f'RCV{i}': [] for i in range(1, 5)}

    # Append RSSI value to the corresponding receiver's list
    average_rssi[location][f'RCV{receiver}'].append(record['RSSI'])

# Calculate the average RSSI for each location and receiver
average_rssi_json = []
for location, receivers in average_rssi.items():
    avg_rssi = {}
    for receiver, rssi_values in receivers.items():
        avg_rssi[receiver] = int(sum(rssi_values) / len(rssi_values)) if rssi_values else 0
    x, y = map(float, location.split(','))
    avg_rssi['X'] = x
    avg_rssi['Y'] = y
    average_rssi_json.append(avg_rssi)

# Write the results to a JSON file
with open('average_rssi.json', 'w') as outfile:
    json.dump(average_rssi_json, outfile, indent=4)

print("Average RSSI data saved to average_rssi.json")

