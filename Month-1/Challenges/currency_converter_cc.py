from currency_converter import CurrencyConverter
c = CurrencyConverter()

def eur_to_usd_fn():
    a = float(input("Digite 1 número para converter: "))
    print(a * 1.16)

def eur_to_usd_cc_fn():
    a = float(input("Digite 1 número para converter: "))
    print(c.convert(a, 'USD'))

# eur_to_usd_fn()
eur_to_usd_cc_fn()