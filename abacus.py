def print_abacus(value):
    i = len(str(value)) - 1
    while i >= 0:
        print("0" * (10 - int(str(value)[i])) + " " + "0" * int(str(value)[i]))
        i -= 1


print_abacus(12345)
