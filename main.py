from graphviz import Digraph

N = 1000
edges = []
memo = {1: True}

def sum_digit_square(n):
    sum = 0
    for i in str(n):
        k = int(i)
        sum += k ** 2
    return sum


def is_happy(n):
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

        next = sum_digit_square(n)
        appeared.append(n)

        edge = (n, next)
        if edge not in edges:
            edges.append((n, next))
        n = next


def main():
    for i in range(1, N):
        if is_happy(i):
            #print(i)
            pass

    G = Digraph(format="png")
    G.attr("node", shape="circle")
    for i,j in edges:
        if memo[i]:
            G.edge(str(i), str(j))
    G.render("output/tree_" + str(N))

if __name__ == "__main__":
    main()
