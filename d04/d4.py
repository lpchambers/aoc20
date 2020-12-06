#!/usr/bin/python3
with open('input') as f:
    l = f.readlines()

# l = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
# 
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
# 
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
# 
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
# """.splitlines()

# l = """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
# 
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
# 
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
# 
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
# 
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
# 
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
# 
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
# 
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".splitlines()

l.append("")

needed = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

d = {}
p1 = 0
p2 = 0
for line in l:
    ll = line.strip()
    if ll == "":
        print(d)
        if all(x in d for x in needed):
            p1 += 1
        else:
            d = {}
            continue

        byrpass = 2002 >= int(d['byr']) >= 1920
        iyrpass = 2020 >= int(d['iyr']) >= 2010
        eyrpass = 2030 >= int(d['eyr']) >= 2020
        hgt = d['hgt']
        if hgt.endswith('in'):
            hgtval = int(hgt[:-2])
            hgtpass = 76 >= hgtval >= 59
        elif hgt.endswith('cm'):
            hgtval = int(hgt[:-2])
            hgtpass = 193 >= hgtval >= 150
        else:
            hgtpass = False
        
        hcl = d['hcl']
        hclpass = len(hcl) == 7 and hcl[0] == '#' and all(x in '0123456789abcdef' for x in hcl[1:])

        ecl = d['ecl']
        eclpass = ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        pid = d['pid']
        pidpass = len(pid) == 9 and all(x in '0123456789' for x in pid)

        print(byrpass)
        print(iyrpass)
        print(eyrpass)
        print(hgtpass)
        print(hclpass)
        print(eclpass)
        print(pidpass)

        if byrpass and iyrpass and eyrpass and hgtpass and hclpass and eclpass and pidpass:
            p2 += 1
        d = {}
        continue

    for part in ll.split():
        k, v = part.split(':')
        d[k] = v

    print(ll)

print(p1)
print(p2)
