f = open("file_for_3.txt", "r")
lines = f.readlines()
for line in lines:
    to_sum, result = line.split(";")


    # calc result
    sum = 0
    num = len(to_sum.split())
    for n in to_sum.split():
        sum += int(n)

        res = sum // num
        ost = sum % num

        # get res
    res_r, ost_r = [int(i) for i in result.split()]

        # compare

    sum_print = " ".join(to_sum.split())
    if res == res_r and ost == ost_r:
        print(f'{sum_print};{res} {ost}, True')
    elif res != res_r or ost != ost_r:
        print(f'{sum_print};{res} {ost}, False')