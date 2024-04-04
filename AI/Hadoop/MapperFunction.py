import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into fields
    fields = line.split(",")
    
    # Extract relevant information from the input fields
    timestamp = fields[0]
    start_location = fields[1]
    end_location = fields[2]
    distance = float(fields[3])
    average_speed = float(fields[4])
    weather_conditions = fields[5]
    road_conditions = fields[6]
    
    # Emit key-value pairs for analysis
    # Key: Start location
    # Value: Timestamp, End location, Distance, Average speed, Weather conditions, Road conditions
    print(f"{start_location}\t{timestamp},{end_location},{distance},{average_speed},{weather_conditions},{road_conditions}")


# Results 
2024-04-01 08:00:00,New York,Los Angeles,2789.5,65.2,Sunny,Light traffic
2024-04-02 10:30:00,San Francisco,Seattle,808.2,55.7,Rainy,Moderate traffic
2024-04-03 12:45:00,Chicago,Miami,1200.7,70.3,Cloudy,Heavy traffic

New York   2024-04-01 08:00:00,Los Angeles,2789.5,65.2,Sunny,Light traffic
San Francisco   2024-04-02 10:30:00,Seattle,808.2,55.7,Rainy,Moderate traffic
Chicago   2024-04-03 12:45:00,Miami,1200.7,70.3,Cloudy,Heavy traffic
