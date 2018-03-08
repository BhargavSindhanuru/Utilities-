def isProbablyPrime(n,k=5):
    '''
    Input: Positive integer n, Optional k=no. of iterations: Accuracy increases with increase in k
    Output: Is n prime? (True/False)

    Uses Fermat's little theorem for k iterations
    '''
    from random import randint
    if n<2:
        return False
    for i in range(k):
        a = randint(1,n-1)
        if pow(a,n-1,n) != 1:
            return False
    return True

