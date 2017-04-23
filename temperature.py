from csv import reader

with open('sensor.csv', 'r') as f:
    data = list(reader(f))
