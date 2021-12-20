def age_assignment(*args, **kwargs):
    new_dict = {}
    for letter, age in kwargs.items():
        for name in args:
            if name[0] == letter:
                new_dict[name] = age
    return new_dict
