def scramble(items):

    for i, item in enumerate(items):

        items[i] = item + i


items = [1, 2, 3]

scramble(items)

print(items)