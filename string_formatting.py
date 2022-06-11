
greeting = "Hello, Bob"
print(greeting)

name = "Rolf"
print(f"Hello, {name}")

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

name = "Rolf"
day = "Monday"
phrase = f"Hello, {name}. Today is {day}"
print(phrase)

phrase = "Hello, {}. Today is {}"
formatted = phrase.format("Dick", "Friday")
print(formatted)
