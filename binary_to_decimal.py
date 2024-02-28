def binary_to_decimal(binary):
    if "0b" in binary:
        binary = binary.replace("", "")
    total = 0
    for i, bit in enumerate(binary[::-1]):
        total += int(bit) * 2 ** i
    return total


if __name__ == "__main__":
    binary = input("Enter your binary number: ")
    try:
        print(binary_to_decimal(binary))
    except:
        print("Error")
