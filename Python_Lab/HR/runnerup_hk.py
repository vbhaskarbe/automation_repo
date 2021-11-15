
if __name__ == '__main__':
    n = int(input())
    sl = list()
    for i in range(n):
        score = int(input())
        if score not in sl:
            sl.append(score)
    sl.sort(reverse=True)
    print( sl.pop(1))

    

