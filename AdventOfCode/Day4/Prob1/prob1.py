necessary_attr = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
def is_valid(line):
    count = 0
    line = line.split(" ")
    headings = []
    for i in line:
        res = i.split(":")
        if len(res) != 0:
            headings.append(res[0])
    for i in necessary_attr:
        if i in headings:
            count += 1
    if count == 7:
        print(f"Passport: {line}")
        return True
    else:
        return False
    
# Using readlines() 
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
print("start")
count = 0
curr_passport = ""
for line in Lines:
    line = line.strip()
    if line == '':
        if is_valid(curr_passport):
            count += 1
        curr_passport = ""
        continue
    else:
        curr_passport += " " + line
if is_valid(curr_passport):
    count += 1

print(f"Total valid passwords: {count}")