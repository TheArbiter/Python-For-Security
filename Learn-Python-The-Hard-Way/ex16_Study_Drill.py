from sys  import argv

script, filename = argv

print(f"The contents of the file {filename}.")

target = open(filename)
contents = target.read()
print(contents)
target.close()
