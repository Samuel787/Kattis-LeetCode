# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
print("start")
count = 0
entries = []
for line in Lines:
    entries.append(int(line.strip()))
entries.sort()
if len(entries) < 3:
    print("impossible")

found = False
for i in range(len(entries)):
    first_num = entries[i]
    remainder = 2020 - first_num
    if i > len(entries) - 2:
        print("impossible")
        break
    start = i + 1
    end = len(entries) - 1
    while start < end:
        if entries[start] + entries[end] == remainder:
            print(f"Result: {entries[start] * entries[end] * first_num}")
            found = True
            break
        elif entries[start] + entries[end] < remainder:
            start += 1
        else:
            end -= 1
    if found:
        break
        

