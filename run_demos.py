
counter = 0
def foo():
    global counter
    counter = counter + 1
    print("Hello")

foo()
foo()

print(counter)

def foo_with_counter():
    foo_with_counter.count = foo_with_counter.count + 1
    print("Hello")


foo_with_counter.count = 0

foo_with_counter()
foo_with_counter()
foo_with_counter()
print(foo_with_counter.count)