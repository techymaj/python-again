def func(a, b, *args, k, **kwargs):
    print("positional-or-named: ", f"{a}", f"{b}")
    print("var-positional (*args): ", f"{args}")
    print("named argument (k): ", f"{k}")
    print("variable named: ", f"{kwargs}")


func(1, 2, "a", "b", "c", k="Trent", key1="Ayra", key2="Stark")
