import sys


#This function will sort a given sequence of numbers
#if value in the list of numbers is not interger or float, program will exit
def sort_numbers(numbers):
    for i, value in enumerate(numbers):
        try:
            numbers[i] = float(value)
        except ValueError:
            print("Error:", value, "is not a valid number.")
            sys.exit(1)
    numbers = [num for num in numbers if num >= 0] + [num for num in numbers if num < 0]
    numbers.sort()
    return numbers


def main():
    numbers_list = input("Enter the numbers separated by space: ").strip().split()
    print(sort_numbers(numbers_list))


if __name__ == "__main__":
    main()
    sys.exit(0)
