from project.leap_year_checker import is_leap_year


def main():
    year = input("Enter a year number: ")
    print("Is", year, "a leap year?", is_leap_year(int(year)))


if __name__ == '__main__':
    main()
