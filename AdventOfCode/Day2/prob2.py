
def is_valid(pwd, c, l, u):
    count = 0
    length = len(pwd)
    l -= 1
    u -= 1
    if l >= 0 and l < length and pwd[l] == c:
        count += 1
    if u >= 0 and u < length and pwd[u] == c:
        count += 1
    if count == 1:
        return True
    else:
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



    
        