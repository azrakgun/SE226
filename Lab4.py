
num_users = int(input("Enter number of users: "))
user_data = {}
for i in range(num_users):
    username = input("Enter username: ")
    num_items = int(input("How many items? "))

    items_list = []
    for j in range(num_items):
        item = input(f"Item {j + 1}: ")
        items_list.append(item)

    user_data[username] = items_list


all_items = []
for items in user_data.values():
    all_items.extend(items)
unique_names = set(all_items)

print("USER DATA:")
for name, items in user_data.items():
    print(f"{name}  {items}")

print("COMMON ITEMS:")

for item in unique_names:
    if all_items.count(item) > 1:
        print(item)

print("UNIQUE ITEMS:")

for item in unique_names:
    if all_items.count(item) == 1:
        print(item)

print("MOST POPULAR ITEM:")

if all_items:
    max_count = 0
    for item in unique_names:
        count = all_items.count(item)
        if count > max_count:
            max_count = count

    for item in unique_names:
        if all_items.count(item) == max_count:
            print(item)


