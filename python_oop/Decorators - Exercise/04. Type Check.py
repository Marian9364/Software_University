def type_check(type_check):
    def decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_check):
                    return "Bad Type"
            return func(*args)
        return wrapper
    return decorator
