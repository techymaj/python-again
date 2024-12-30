def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')
    print(f"greet_pythons: {locals()}")

    def make_greeting(i: str) -> str:
        nonlocal greeting  # greeting is now the same object as the enclosed one
        greeting = 'Hi'
        print(f"make_greeting: {locals()}")
        print(f'The ID of `greeting` in `make_greeting` is {id(greeting)}')
        return f'{greeting} {i}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, `greeting` is {greeting}')
    print(f'The ID of `greeting` in `greet_pythons` is {id(greeting)}')


names = ['John']  # , 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
