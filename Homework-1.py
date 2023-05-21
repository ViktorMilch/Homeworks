import time
from functools import wraps

def make_frame(funct):
    @wraps(funct)
    def wrapper(*abcd, **efg):
        print("*" * 10)
        result = funct(*abcd, **efg)
        print("*" * 10)
        return result
    return wrapper

def time_it(funct):
    @wraps(funct)
    def wrapper():
        start = time.time()
        funct()
        finish = time.time() - start
        print(finish)
        return funct()
    return wrapper

@time_it
@make_frame

def show():
    """there should be some text here"""
    lines = [input() for i in range(5)]
    f_lines = filter(lambda a: len(a) >= 3, lines)
    f_lines = filter(lambda a: "a" in a or "A" in a, lines)
    u_lines = map(lambda a: a.upper(), f_lines)
    return tuple(u_lines)

print(show.__doc__)
result = show()
print(result)