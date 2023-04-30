def power(base,exp):
    assert 0 <= exp == int(exp), 'The exponent must be positive integer only!'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base,exp-1)
power(2,4)
