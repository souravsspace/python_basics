# item_list = []
# item_list = ["Sourav", 21, False, 62.5]

# print(item_list)

# name = "SOuRAv"
# print(name.capitalize() in item_list)

# print(len(item_list))
# print(item_list[1])
# item_list[1] = "Ukil"
# print(item_list[1])

# print(item_list[-2])
# print(item_list[-2:2])
# print(item_list[1:3])

# item_list.append("Kolkata")
# item_list.remove(21)
# print(item_list)

# new_list = ["Ratul", 23, True, 52.5]
# item_list.extend(new_list)
# item_list += new_list
# print(item_list)

# print(item_list)
# print(item_list.pop(-0))
# print(item_list.pop(-1))
# print(item_list.pop(-2))
# print(item_list)
# item_list.clear()
# print(item_list)

# item_list.insert(2, "Dhaka")
# item_list[1:2] = ["Dhaka", "BD"]
# print(item_list)


# items = [45, 99, 13, 34, 55, 1009, 234]
# items.sort()

items = ["Sourav", "ratul", "amit", "Airin"]

# items_copy = items.copy()
# items.sort(key=str.lower)
print(sorted(items, key=str.lower))
print(items)
# print(items_copy)
