necessary_attr = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def check_valid_hair_color(code):
    codes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
     'a', 'b', 'c', 'd', 'e', 'f']
    if len(code) == 7:
        if code[0] == '#':
            for i in code[1:]:
                if i not in codes:
                    return False
            return True
        else:
            return False
    else:
        return False

def is_valid(line):
    count = 0
    line = line.split(" ")
    headings = {}
    for i in line:
        if i == "":
            continue
        res = i.split(":")
        if len(res) != 0:
            headings[res[0]] = res[1]
    
    if 'byr' in headings:
        try:
            val = int(headings['byr'])
            if not (val >= 1920 and val <= 2002):
                return False
        except Exception as e:
            return False
    else:
        return False

    if 'iyr' in headings:
        try:
            val = int(headings['iyr'])
            if not (val >= 2010 and val <= 2020):
                return False
        except Exception as e:
            return False
    else:
        return False
    
    if 'eyr' in headings:
        try:
            val = int(headings['eyr'])
            if not (val >= 2020 and val <= 2030):
                return False
        except Exception as e:
            return False
    else:
        return False
    
    if 'hgt' in headings:
        if len(headings['hgt']) < 3:
            return False
        unit = headings['hgt'][-2:]
        val = headings['hgt'][:-2]
        if unit == "cm":
            try:
                val = float(val)
                if not (val >= 150 and val <= 193):
                    return False
            except Exception as e:
                return False
        elif unit == "mm":
            try:
                val = float(val)
                if not (val >= 59 and val <= 76):
                    return False
            except Exception as e:
                return False
        else:
            return False
    else:
        return False

    if 'hcl' in headings:
        if not check_valid_hair_color(headings['hcl']):
            return False
    else:
        return False

    if 'ecl' in headings:
        val = headings['ecl']
        if val not in ecl_list:
            return False
    else:
        return False

    if 'pid' in headings:
        val = headings['pid']
        if len(val) == 7:
            try:
                val = int(val)
            except Exception as e:
                return False
        else:
            return False
    else:
        return False

    return True
    
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

print(f"Total valid passports: {count}")