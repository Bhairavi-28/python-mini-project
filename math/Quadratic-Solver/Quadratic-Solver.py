from math import sqrt, isqrt, gcd
from fractions import Fraction

print("\n\n", "=" * 20, " QUADRATIC EQUATION SOLVER ", "=" * 20)
print(
    "\nEasily find the roots of a quadratic equation in the form of ax^2 + bx + c = 0."
)
print("Input format should be: a, b, c\n")


def rational_roots(a, r, b):
    x1 = Fraction(-b + r, 2 * a)
    x2 = Fraction(-b - r, 2 * a)
    print(f"🟢 Exact form:\n💠 {x1}\n💠 {x2}\n")
    print(f"🟢 Decimal form:\n💠 {float(x1):.4f}\n💠 {float(x2):.4f}\n")


def irrational_roots(a, r, b):
    pass


def find_roots(coeffs):
    a, b, c = coeffs

    d = b * b - 4 * a * c

    # REAL ROOTS
    if d >= 0:
        radical = sqrt(d)
        radical_int = isqrt(d)
        # Rational roots
        if radical_int * radical_int == d:
            rational_roots(a, radical_int, b)
        # Irrational roots
        else:
            irrational_roots(a, radical, b)
    # COMPLEX ROOTS
    else:
        pass


# User Input
inp = input("Enter a,b,c: ")
coeffs = [int(i.strip()) for i in inp.split(",") if i.strip()]

find_roots(coeffs)
