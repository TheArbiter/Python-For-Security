import sys
script, input_encoding, error = sys.argv

#main function
def main(language_file, encoding, errors):
    #Read one line from the file
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    #strip() if a set of characters are specified it would remove that
    #if no characters specified then it removes the leading and trailing white spaces
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
