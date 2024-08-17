# Concise, idiomatic way to count things in Python

count = {}
for item in things:
    if item not in count:
        count[item] = 0
    count[item] += 1