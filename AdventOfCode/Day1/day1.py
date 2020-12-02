# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
print("start")
count = 0
entries = {}
for line in Lines:
    print("reading")
    curr_num = int(line.strip())
    pair_num = 2020 - curr_num
    if pair_num in entries:
        print(f"The answer is: {pair_num * curr_num}")
        break
    entries[curr_num] = 1
print(f"Dictionary: {entries}")


    
        