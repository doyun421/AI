import sys

# Input comes from STDIN (standard input)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into fields
    fields = line.split(",")
    
    # Extract relevant information from the input fields
    timestamp = fields[0]
    patient_id = fields[1]
    arm_id = fields[2]
    cancer_type = fields[3]
    procedure_details = fields[4]
    surgical_outcome = fields[5]
    
    # Emit key-value pairs for analysis
    # Key: Patient ID
    # Value: Timestamp, Arm ID, Cancer Type, Procedure Details, Surgical Outcome
    print(f"{patient_id}\t{timestamp},{arm_id},{cancer_type},{procedure_details},{surgical_outcome}")


2024-04-01 08:00:00,P123,A1,Breast,Incision at quadrant 2,Success
2024-04-02 09:30:00,P124,A2,Lung,Excision depth of 2 cm,Success
2024-04-03 10:45:00,P125,A3,Colon,Excision at tumor site,Failure

P123	2024-04-01 08:00:00,A1,Breast,Incision at quadrant 2,Success
P124	2024-04-02 09:30:00,A2,Lung,Excision depth of 2 cm,Success
P125	2024-04-03 10:45:00,A3,Colon,Excision at tumor site,Failure
