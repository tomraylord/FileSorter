import os, time, shutil
# os: path handling
# time: sleeping at the end
# shutil: moving files easier

# Get current working directory
cwd = os.getcwd()

# Track files that couldn't be moved
clash = 0
clashes = []

# Loop through every file in the cwd
for file in os.listdir():
    # Make sure that the file is not the python script
    if file == os.path.basename(__file__):
        continue

    # Make sure that the file is not a folder
    if os.path.isfile(file):
        # Split path into name and extension
        name, ext = os.path.splitext(file)
        # Ensure lowercase and remove .
        ext = ext.replace('.', '').lower()

        # Add extension if the file does not have one
        if ext == "":
            ext = "file"

        # Create directory to be made
        dir = os.path.join(cwd, ext)

        # Check that the directory does not exist before running it
        if not os.path.exists(dir):
            # Make the directory
            os.makedirs(dir)

        # Prevent overwriting existing file
        if not os.path.exists(dir + "\\" + file):
            # Move file
            shutil.move(cwd + "\\" + file, dir + "\\" + file)
        else:
            # Track files that cannot be moved
            clash += 1
            clashes.append(name + ext)

# Output result
if clash == 1:
    print('Finished with 1 clash: ')
else:
    print('Finished with ' + clash + 'clashes: ')

# List all clashes
for cl in clashes:
    print(" - " + cl)

# Sleep so that the user can see the info
time.sleep(15)
