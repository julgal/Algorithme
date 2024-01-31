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

my_list = [1,5,4,3,8,9,45,23,22,67,56,89,7,500,400,600,1000,998,788]
print(my_list)
print(bubble_sort(my_list))
