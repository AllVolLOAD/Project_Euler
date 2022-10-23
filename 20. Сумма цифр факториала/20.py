"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
"""


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

fac_to_str = str(fac(100))
print(fac_to_str, type(fac_to_str))
print(sum(int(i) for i in fac_to_str))

