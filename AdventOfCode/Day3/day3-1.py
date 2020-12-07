
# Using readlines()
file1 = open("input.txt", 'r')
Lines = file1.readlines()
map = []
for line in Lines:
    map.append(line.strip())

count = 0
step = 0
i = 0
j = 0
width = len(map[0])
while i < len(map):
    if map[i][j] == '#':
        count += 1
    j += 3
    j %= width
    i += 1

print(f"Total number of trees: {count}")

