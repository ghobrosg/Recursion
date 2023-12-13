def getfactorial(n: int) -> int:
    """
    >>> getfactorial(5)
    120
    >>> getfactorial(0)
    1
    >>> getfactorial(1)
    1
    >>> getfactorial(-3)
    -1
    """
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return getfactorial(n-1) * n
