def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        flag = 0
        for j in range(n - 1):
            if lst[j + 1] < lst[j]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
                flag = 1
        if flag == 0:
            break
    return lst

if __name__ == "__main__":
    try:
        list_n = []
        numbers = input("Enter list numbers:")
        for number in numbers.split():
            list_n.append(int(number))

        print(bubble_sort(list_n))
    except:
        print("Error, You have not enter a number.")
