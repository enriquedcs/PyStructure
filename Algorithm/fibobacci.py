

def fibonacci(num):
    sum1 = 0
    L = [0, 1]
    for i in range(1, num):
        L.append(L[-1] + L[-2])

    if L[-1] > 4000000:
        return False
    else:
        print(L)
        for i in range(1, num):
            if L[i] % 2 == 0:
                sum1 = L[i] + sum1
    return sum1


num = 33
print(fibonacci(num))
