import os

# Directory path
directory = os.path.dirname(os.path.abspath(__file__)) + "\logs"
print(directory)


# Initialize an empty list to store file names
log_files = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the current item is a file
    if os.path.isfile(os.path.join(directory, filename)):
        # Add the file name to the list
        log_files.append("logs\\" + filename)

login_lines = []
for file_path in log_files:
    # Open the file
    with open(file_path, 'r') as file:
        # Read and process each line
        for line in file:
            # Do something with the line
            if line.find("Authenticate:") !=-1:
                print(line)
                login_lines.append(line)



# Open the file in write mode
with open("logins.txt", 'w') as file:
    # Iterate over the strings
    for login_line in login_lines:
        # Write the string to the file followed by a newline character
        file.write(login_line + '\n')

