import time

def func(f):
    def wrapper(*args, **kwargs):
        print("Started...")
        rv = f(*args, **kwargs)
        print("Ended")
        return rv

    return wrapper

@func
def func2(x, y):
    print(x)
    return y

@func
def func3():
    print("Iam func3")

# x = func(func2)
# x()

# func2 = func(func2)
# func3 = func(func3)

# func2(67, 4)
# x = func2(4,90)
# print(x)

# func3()

# decorator application
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("Total time: ", total)
        return rv
    return wrapper

@timer
def test():
    for _ in range(100000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()