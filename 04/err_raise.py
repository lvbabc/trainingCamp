import logging
logging.basicConfig(level=logging.INFO)


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    if n == 0:
        raise ValueError(f'invalid value: {s}')
    return 10 / n


# foo('0')


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise


# bar()

s = '0'
n = int(s)
logging.info(f'n = {n}')
print(10 / n)
