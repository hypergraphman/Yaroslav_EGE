for n in range(5, 36 + 1):
    for x in range(-10000, 10000):
        formula = f'{x**2} - {int("30", n)} * {x} + {int("240", n)}'
        if eval(formula) == 0:
            print(n, x)
