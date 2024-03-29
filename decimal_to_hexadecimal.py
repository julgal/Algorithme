def decimal_to_hexadecimal(n):
    hexadecimal = ""
    hexa_values = {
            "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
            "6": "6", "7": "7", "8": "8", "9": "9", "10": "A", "11": "B",
            "12": "C", "13": "D", "14": "E", "15": "F"}

    while n > 0:
        hexadecimal = hexa_values[str(n%16)] + hexadecimal
        n = n // 16
    return hexadecimal


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        print(decimal_to_hexadecimal(n))
    except:
        print("Error.")
