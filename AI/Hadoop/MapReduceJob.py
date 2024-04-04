import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into fields
    fields = line.split(",")
    
    # Extract relevant information from the input fields
    origin = fields[0]  # Origin location of the car
    destination = fields[1]  # Destination location of the car
    distance = float(fields[2])  # Distance traveled by the car
    
    # Emit key-value pairs for analysis
    # Key: Origin location
    # Value: Destination location, Distance traveled
    print(f"{origin}\t{destination},{distance}")






## results
New York,Los Angeles,2789.5
San Francisco,Seattle,808.2
Chicago,Miami,1200.7

New York   Los Angeles,2789.5
San Francisco   Seattle,808.2
Chicago   Miami,1200.7
##
