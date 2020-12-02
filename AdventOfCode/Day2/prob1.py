
def is_valid(pwd, c, l, u):
    count = 0
    for i in range(len(pwd)):
        if pwd[i] == c:
            count += 1
    if count >= l and count <= u:
        return True
    return False
    
# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
print("start")
count = 0
for line in Lines:
    line = line.strip().split(" ")
    first = line[0].split("-")
    second = line[1]
    third = line[2]
    
    lower = int(first[0])
    upper = int(first[1])
    letter = second[0]
    pwd = third
    if(is_valid(pwd, letter, lower, upper)):
        count += 1

print(f"Total valid passwords: {count}")



    
        