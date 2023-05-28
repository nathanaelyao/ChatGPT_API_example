def read_file_contents(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents