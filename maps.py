from timeit import timeit


def at():
    atlas = map(lambda x: x ** 2, [1, 2, 4, 6, 8])
    return [*atlas]


def proj_at():
    return [x ** 2 for x in [1, 2, 4, 6, 8]]


time_atlas = timeit(at, number=100_000_000)
time_project_atlas = timeit(proj_at, number=100_000_000)

print(time_atlas)
print(time_project_atlas)
