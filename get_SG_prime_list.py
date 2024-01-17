def is_prime(nb):
        if nb < 2:
                return False
        for d in range(2, nb):
                if nb % d == 0:
                        return False
        return True

def is_SG_prime(nb):
        if is_prime(nb) and is_prime(nb*2+1):
                return True
        else:
                return False

def get_SG_prime_list(inf, sup):
        list_SG_prime = []
        for nb in range(inf, sup+1):
                if is_SG_prime(nb):
                        list_SG_prime.append(nb)
        return list_SG_prime
