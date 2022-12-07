import math

n = int(input())

sqrt1 = math.isqrt(n)
sqrt2 = math.sqrt(n)

if sqrt2 ** 2 < n: #n이 큰 수일 경우 부동소수점 오차 발생
    print(int(sqrt2) + 1)
elif float(sqrt1) == sqrt2:
    print(sqrt1)
else:
    print(sqrt1 + 1)