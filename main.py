def convert_to_binary(number: int, num_bits: int) -> str:
    return bin(number)[2:].zfill(num_bits)


def convert_bin_to_negative(number: str) -> str:
    pass


def main():
    number = int(input("Enter a number: "))
    bits_amount = int(input("Enter the amounts of bits: "))
    bin_number = convert_to_binary(number, bits_amount)
    print(bin_number)
    negative_bin_number = convert_bin_to_negative(bin_number)
    print(negative_bin_number)
    


if __name__ == "__main__":
    main()