def reverse_bin_nbr(nbr):
    if isinstance(nbr, int):
        nbr = bin(nbr)
    if "0b" in nbr:
        nbr = nbr.replace("0b", "")

    new_nbr = ""
    for bit in nbr:
        if bit == "0":
            new_nbr += "1"
        else:
            new_nbr += "0"

    return new_nbr
