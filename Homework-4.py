
# def decorate(func):
#     def wrapper(arg):
#         print("=" * (10 + len(arg)))
#         func(arg)
#         print("=" * (10 + len(arg)))
#     return wrapper
    
    
# @decorate
# def welcome(name):
#     print(f"Hello {name}")
    
# welcome("Artem")

# def show():
#     lines = [input() for i in range(5)]
#     return lines
# print(show)

# print(show.__doc__)
# print(show()):
     

# > python lesson5.py

#     Reads 5 strings from input
#     Returns upper-cased strings that contain `A`
#     and are at least 3 characters long

# **********
# teach
# me
# skills
# aA
# ABOBA
# **********
# It took 11.392664909362793 seconds
# ('TEACH', 'ABOBA')
# import time

# def time_it(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Time taken: {end - start:.6f}s")
#         return result
#     return wrapper

# def make_frame(func):
#     def wrapper
#         print("**********")
#         result = func(*args, **kwargs)
#         print("**********")
#         return result
#     return wrapper
def time_it(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        

def make_frame(func):
    def wrapper(a,b):
        print("*" * 10)
        result = func(a,b)
        print("*" * 10)
        return result
    return wrapper

@time_it
@make_frame
def show():
    lines = [input() for i in range(5)]
    f_lines = filter(lambda a: len(a) >= 3, lines)
    f_lines = filter(lambda a: "a" in a or "A" in a, lines)
    u_lines = map(lambda a: a.upper(), f_lines)
    return tuple(u_lines)
result = show()
print(result)




    
def show():
    lines = [input() for i in range(5)]:
    f_lines = filter(lambda a: len())