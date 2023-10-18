import string

# Define the input and output file paths
input_file = 'rockyou.txt'
output_file = 'processed_rockyouv2.dic'

# Open the input and output files
with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(output_file, 'w') as outfile:
    # Loop through each line in the input file
    for line in infile:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check if the line contains non-ASCII characters
        if not all(c in string.printable for c in line):
            # Skip lines with non-ASCII characters
            continue

        # Check if the line starts with a digit
        if line and line[0].isdigit():
            # Discard lines starting with a digit
            continue

        # Capitalize the first letter, add '0' to the end, and write to the output file
        processed_line = line.capitalize() + '0\n'
        outfile.write(processed_line)

print(f"Processing complete. Result saved to {output_file}")

