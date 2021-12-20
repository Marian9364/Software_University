def func_executor(*args):
    results = []
    for func, tup in args:
        results.append(func(*tup))
    return results
