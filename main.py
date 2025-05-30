def convert_to_binary(number:int) -> str:
    pass

def convert_bin_to_negative(number: str) -> str:
    pass


def main():
    number = int(input("Enter a number: "))
    bin_number = convert_bin_to_negative(number)
    negative_bin_number = convert_bin_to_negative(bin_number)
    print(negative_bin_number)


if __name__ == "__main__":
    main()