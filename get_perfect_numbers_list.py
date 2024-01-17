def get_dividers(nb):
        dividers_list = []
        for divider in range(1, nb+1):
                if nb % divider == 0:
                        dividers_list.append(divider)
        return dividers_list

def is_perfect(nb):
        if sum(get_dividers(nb)[:-1]) == nb:
                return True
        return False

def get_perfect_numbers_list(inf, sup):
        perfect_numbers_list = []
        for i in range(inf, sup+1):
                if is_perfect(i):
                        perfect_numbers_list.append(i)
        return perfect_numbers_list
