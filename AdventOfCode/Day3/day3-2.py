# Using readlines()
file1 = open("input.txt", 'r')
Lines = file1.readlines()
map = []
for line in Lines:
    map.append(line.strip())

count = [0, 0, 0, 0, 0]
width = len(map[0])
i = 0
j = 0
while i < len(map):
    if map[i][j] == '#':
        count[0] += 1
    j += 1
    j %= width
    i += 1

i = 0
j = 0
while i < len(map):
    if map[i][j] == '#':
        count[1] += 1
    j += 3
    j %= width
    i += 1

i = 0
j = 0
while i < len(map):
    if map[i][j] == '#':
        count[2] += 1
    j += 5
    j %= width
    i += 1

i = 0
j = 0
while i < len(map):
    if map[i][j] == '#':
        count[3] += 1
    j += 7
    j %= width
    i += 1

i = 0
j = 0
while i < len(map):
    if map[i][j] == '#':
        count[4] += 1
    j += 1
    j %= width
    i += 2

result = 1
for i in count:
    result *= i

print(f"Total number of trees: {result}")

