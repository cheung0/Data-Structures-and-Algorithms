def fibNaive(n):
    if n <= 2:
        f = 1
    else:
        f = fibNaive(n - 1) + fibNaive(n - 2)
    return f


memo = {}
def fibTopDown(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fibTopDown(n - 1) + fibTopDown(n - 2)
    memo[n] = f
    return f


def fibBottomUp(n):
    fib = {}

    for k in range(1, n + 1):
        if k <= 2:
            f = 1
        else:
            f = fib[k - 1] + fib[k - 2]
        fib[k] = f

    return fib[n]
