from timeit import timeit

def add(items):
    result = ""
    for item in items:
        result += item
    return result

huge_list = ["hi"] * 10
print(timeit('add(huge_list)', 'from __main__ import add, huge_list'))
print(timeit('"".join(huge_list)', 'from __main__ import add, huge_list'))
