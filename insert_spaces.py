import sys


#This function will takes a string input and inserts spaces between words that start with capital letters:
def insert_spaces(string):
    new_string = string[0]
    for i in range(1, len(string)):
        if string[i].isupper():
            new_string += ' ' + string[i]
        else:
            new_string += string[i]
    return new_string


def main():
    string_input = input("Enter a string: ")
    print(insert_spaces(string_input))


if __name__ == "__main__":
    main()
    sys.exit(0)
