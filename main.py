def convert_to_binary(number: int, num_bits: int) -> str:
    return bin(number)[2:].zfill(num_bits)


def convert_bin_to_negative(number: str) -> str:
    inverted_number = ["0" if digit == "1" else "1" for digit in number]
    for i in range(1, len(inverted_number) + 1):
        index = len(inverted_number) - i
        if inverted_number[index] == "0":
            inverted_number[index] = "1"
            break
        else:
            inverted_number[index] = "0"
            
    return ''.join(inverted_number)


def main():
    number = int(input("Enter a number: "))
    if number <= 0:
        raise Exception("only positive numbers can be entered")
    
    bits_amount = int(input("Enter the amounts of bits: "))
    bin_number = convert_to_binary(number, bits_amount)
    negative_bin_number = convert_bin_to_negative(bin_number)

    print(negative_bin_number)
    


if __name__ == "__main__":
    main()