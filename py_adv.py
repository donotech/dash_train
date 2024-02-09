
class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
result = add_five(6)
print(result)


def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)

generator_exp = (i * 5 for i in range(5) if i % 2 == 0)
generator_exp2 = [i * 5 for i in range(5) if i % 2 == 0]
for i in generator_exp:
    print(i)


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b

    # Create a generator object


fibfoo = fib(5)

# Iterating over the generator object using next
# In Python 3, __next__()
print(next(fibfoo))
print(next(fibfoo))
print(next(fibfoo))
print(next(fibfoo))
print(next(fibfoo))

# list comprehension

newlist = [x * x for x in range(10) if x < 5]
print(newlist)

# closure
def calculate():
    num = 1

    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func


# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())



def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)


def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")


def do_twice_with_params(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice_with_params
def say_whee2(word):
    print("Whee!" + word)


say_whee2("Go")
