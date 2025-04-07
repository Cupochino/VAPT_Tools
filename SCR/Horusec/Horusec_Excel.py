import pandas as pd

# Function to parse the text file
def parse_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # List to hold the extracted data
    data = []
    temp_data = {}
    description = []
    
    for line in lines:
        line = line.strip()
        
        # Skip lines containing only '=============='
        if "==============" in line:
            continue

        # Parse relevant details from the text file
        if line.startswith("Severity:"):
            if temp_data:
                # Add the previous entry to the data
                temp_data['Description'] = "\n".join(description).strip()
                data.append(temp_data)
            # Reset for the new entry
            temp_data = {
                'Severity': line.split(":")[1].strip(),
                'Vulnerability': "",
                'Line': "",
                'File': "",
            }
            description = []  # Clear the description for the new block
        
        elif line.startswith("Line:"):
            temp_data['Line'] = line.split(":")[1].strip()
        
        elif line.startswith("File:"):
            temp_data['File'] = line.split(":")[1].strip()

        elif line.startswith("Details:"):
            temp_data['Vulnerability'] = line.split(":")[1].strip()
            description = []  # Start a new description section after "Details"
        
        elif line and not line.startswith("Language:"):  # Non-empty line that is part of the description
            description.append(line.strip())

    # Add the last entry to data (if there's any data left to process)
    if temp_data:
        temp_data['Description'] = "\n".join(description).strip()
        data.append(temp_data)

    return data

# Function to export data to Excel
def export_to_excel(data, output_file):
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Sort the DataFrame by 'Severity' and 'Vulnerability' alphabetically
    df = df.sort_values(by=['Severity', 'Vulnerability'], ascending=[True, True])

    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)

# Ask user for the input and output file paths
input_file = input("Please enter the path to the input text file: ").strip()
output_file = input("Please enter the path to save the output Excel file (e.g., output_file.xlsx): ").strip()

# Parse the text file
parsed_data = parse_text_file(input_file)

# Export the parsed data to Excel
export_to_excel(parsed_data, output_file)

print(f"Data has been successfully written to {output_file}")
