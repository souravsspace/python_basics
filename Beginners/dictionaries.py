# cat = {"name": "Simbu", "age": 1}
cat = {"name": "Simbu", "age": 1, "color": "blue"}


# print(cat["name"])
# print(cat["age"])

# print(cat.get("color", "Golden or B&W"))

# cat["name"] = "Minu"

# cat.pop("color")
# cat.popitem()
# cat.__setitem__("colors", "Golden")

# print("color" in cat)
# print(cat)

# print(cat.keys())
# print(list(cat.keys()))
# print(cat.values())
# print(list(cat.values()))
# print(list(cat.items()))
# print(len(cat))

cat["fav_food"] = "Fish"

# print(list(cat.items()))

catCopy = cat.copy()

del catCopy["color"]

print(cat)
print(catCopy)
