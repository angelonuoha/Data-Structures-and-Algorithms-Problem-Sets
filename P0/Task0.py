arr = [9, 8, 9, 8]
i = 2
output = [[], [8]]

current = []
current.append(arr[i])
print(current)
current.extend([])
print(output)
print(current)
output.append(current)
print(output)