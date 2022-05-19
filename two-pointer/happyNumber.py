def happyNumber(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sumOfSquares(n)
        if n == 1:
            return True
    return False

def sumOfSquares(n):
    res = 0
    while n:
        digit = n % 10
        res += digit * digit
        n = n // 10
    return res

print(happyNumber(19))