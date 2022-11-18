expanses = [100, 200, 300, 400, 500]
total = 0
for item in expanses:
    total += item
print("Total expanses: {}\n".format(total))

for i in range(len(expanses)):
    print("Month: {}, Expanses: {}".format(i+1, expanses[i]))
    total += expanses[i]
print("Total expanses: {}".format(total))
