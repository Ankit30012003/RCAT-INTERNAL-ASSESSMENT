def read_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return None

filename = "example.txt"  
file_data = read_from_file(filename)
if file_data:
    print("File content:")
    print(file_data)

"""
output:-The file 'example.txt' does not exist.
"""
