a = 'Hi'
a = 45

def sum_and_product_of(a: list, b: tuple) -> None:
    return a + b
c = sum_and_product_of(3, 4)
c = sum_and_product_of("Hi", ' there')

sum_and_product_of()
print(c)