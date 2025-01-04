from timeit import timeit

mixology = {
    1,
    "me",
    None,
    True,
    (3, 4, 5)
}


def transform(param: set):
    new_set = {*""}
    for item in param:
        new_set.update({str(item)})
    return new_set


def transform_comp(param: set):
    return {str(item) for item in param}


transformed = transform(mixology)
transformed_comp = transform_comp(mixology)
print(transformed)
print(transformed_comp)

timed = timeit("transform(mixology)",
               "from __main__ import mixology, transform",
               number=100)

timed_comp = timeit("transform_comp(mixology)",
                    "from __main__ import mixology, transform_comp",
                    number=100)

print(timed)
print(timed_comp)
