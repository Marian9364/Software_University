def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or not arg % 2 == 0:
                return "Please use only even numbers!"
        return func(*args)
    return wrapper
