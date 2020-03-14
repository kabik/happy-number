N = 1000000
memo = {1: True}

def is_happy(n):
    #print(memo)
    appeared = []

    while True:
        if n == 1 or (n in memo and memo[n]):
            for i in appeared:
                memo[i] = True
                memo[n] = True
            return True
        elif n in appeared or (n in memo and memo[n]):
            for i in appeared:
                memo[i] = False
                memo[n] = False
            return False

        appeared.append(n)

        sum = 0
        for i in str(n):
            k = int(i)
            sum += k ** 2

        n = sum


for i in range(1, N):
    if is_happy(i):
        pass
        #print(i)
