source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, "r") as src:
        content = src.read()

    with open(destination_file, "w") as dest:
        dest.write(content)

    print(f" Contents copied from '{source_file}' to '{destination_file}' successfully!")

except FileNotFoundError:
    print(" Source file not found. Please check the file name.")
