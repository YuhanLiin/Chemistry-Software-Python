from math import sqrt

def gcf (numbers):
    numbers = sorted(numbers)
    smaller = numbers[0]
    s_factors, b_factors = [],[]
    for n in range(1, int(sqrt(smaller))+1):
        if smaller%n == 0:
            s_factors.append(n)
            b_factors.append(smaller/n)
    factors = b_factors + s_factors[::-1]
    for f in factors:
        common = True
        for n in numbers[1:]:
            if n%f != 0:
                common = False
                break
        if common:
            return f
            


