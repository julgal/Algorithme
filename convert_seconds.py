def convert_seconds(seconds):
    hours = seconds // 3600
    seconds = seconds -3600 * hours

    minutes = seconds // 60
    seconds = seconds - minutes * 60
    return hours, minutes, seconds

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the number of seconds:"))
        result = convert_seconds(seconds)
        print(f"{result[0]}h {result[1]}m {result[2]}s")
    except:
        print("Error, you don't have enter a number.")
