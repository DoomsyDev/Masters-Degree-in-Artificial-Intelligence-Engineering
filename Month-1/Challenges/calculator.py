def my_add_fn():
    a, b = map(int, input("Digite 2 números separados por espaço: ").split())
    print("SUM: %s" % (a + b))


def my_subtract_fn():
    a, b = map(int, input("Digite 2 números separados por espaço: ").split())
    print("SUBTRACT: %s" % (a - b))


def my_divide_fn():
    a, b = map(int, input("Digite 2 números separados por espaço: ").split())

    if b == 0:
        print("Não é possível dividir por zero!")
    else:
        print("DIVIDE: %s" % (a / b))


def my_multiply_fn():
    a, b = map(int, input("Digite 2 números separados por espaço: ").split())
    print("MULTIPLY: %s" % (a * b))


def my_quit_fn():
    raise SystemExit


def invalid():
    print("INVALID CHOICE!")


menu = {
    "1": ("Sum", my_add_fn),
    "2": ("Subtract", my_subtract_fn),
    "3": ("Divide", my_divide_fn),
    "4": ("Multiply", my_multiply_fn),
    "5": ("Quit", my_quit_fn)
}


for key in sorted(menu.keys()):
    print(key + ": " + menu[key][0])


ans = input("Make A Choice: ")

menu.get(ans, (None, invalid))[1]()
