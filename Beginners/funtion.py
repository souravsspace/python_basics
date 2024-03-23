# def hello(name="world"):
#     print(f"Hello, {name}!")


# hello("Sourav")
# hello("Rue")
# hello()


# def call_hello(name, age):
#     if age < 18:
#         print(f"Hello, {name}! You are not allowed to enter.")
#     elif age == 18:
#         print(
#             f"Hello, {name}! You are allowed to enter, but you are not allowed to drink."
#         )
#     else:
#         print(f"Hello, {name}! You are allowed to enter and drink.")


# call_hello("Sourav", 21)
# call_hello("Rue", 18)


# def change_name(value):
#     value["name"] = "Sourav"


# value = {"name": "Rue"}

# change_name(value)
# print(value)


# def hello(name: str):
#     if not name:
#         return "You did not enter a name!"
#     return f"Hello, {name}!"


# print(hello("Sourav Ukil"))
# print(hello(334))


# def talk(phrase=str):
#     def say(word):
#         return f"{word}"

#     words = phrase.split(" ")
#     for word in words:
#         print(say(word))


# talk("Hello, how are you?")


# def counts():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         print(count)

#     increment()


# counts()


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


increment = counter()

print(increment())
print(increment())
