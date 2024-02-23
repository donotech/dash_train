def my_decorator(func, *args, **kwargs):
    # print(param)

    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")

    return wrapper


def say_hello():
    print("HELLO")


@my_decorator(param=10)
def say_decorated_hello(w="Something"):
    print("DECORATED_HELLO" + w)


foo = my_decorator(say_hello)
foo()
print("===================")
say_decorated_hello()
