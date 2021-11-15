
if __name__ == '__main__':
    full_list = []
    values    = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        full_list.append( [name, score])
    for x in full_list:
        full_list.sort(key = lambda x: x[1])
        if float(x[1]) not in values:
            print(x[1])
            values.append(x[1])

    print(values)
    values.sort()
    second_low = values[1]
    out_list   = []

    print(second_low)
    for x in full_list:
        if x[1] == second_low:
            out_list.append(x[0])
            out_list.sort()
    [ print(x) for x in out_list]


