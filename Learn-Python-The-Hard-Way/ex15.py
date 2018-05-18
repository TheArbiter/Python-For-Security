from sys import argv

script, filename = argv

txt = open(filename)

#Read file name from argument passed
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

#Read file from input prompt 
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
