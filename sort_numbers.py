import sys


#This function will sort a given sequence of numbers
#if value in the list of numbers is not interger or float, program will exit
def sorting_numbers(numbers):
    for i, value in enumerate(numbers):
        try:
            if float(value).is_integer():
                numbers[i] = int(value)
            else:
                numbers[i] = float(value)
        except ValueError:
            print("Error:", value, "is not a valid number.")
            sys.exit(1)
    numbers.sort()
    return numbers


def main():
    numbers_list = input("Enter the numbers separated by space: ").strip().split()
    print(sorting_numbers(numbers_list))


if __name__ == "__main__":
    main()
    sys.exit(0)
