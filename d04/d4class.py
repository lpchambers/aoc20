#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

lines.append("")

needed = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]


class Passport:
    def __init__(self, d):
        self.d = d

    def has_fields(self):
        return all(x in self.d for x in needed)

    def is_valid(self):
        if not self.has_fields():
            return False

        byrpass = 2002 >= int(self.d['byr']) >= 1920
        iyrpass = 2020 >= int(self.d['iyr']) >= 2010
        eyrpass = 2030 >= int(self.d['eyr']) >= 2020
        hgt = self.d['hgt']
        if hgt.endswith('in'):
            hgtval = int(hgt[:-2])
            hgtpass = 76 >= hgtval >= 59
        elif hgt.endswith('cm'):
            hgtval = int(hgt[:-2])
            hgtpass = 193 >= hgtval >= 150
        else:
            hgtpass = False
        
        hcl = self.d['hcl']
        hclpass = len(hcl) == 7 and hcl[0] == '#' and all(x in '0123456789abcdef' for x in hcl[1:])

        ecl = self.d['ecl']
        eclpass = ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

        pid = self.d['pid']
        pidpass = len(pid) == 9 and all(x in '0123456789' for x in pid)

        return all([byrpass, iyrpass, eyrpass, hgtpass, hclpass, eclpass, pidpass])


passports = []

d = {}
for line in lines:
    if line == "":
        passports.append(Passport(d))
        d = {}
    else:
        for part in line.split():
            k, v = part.split(':')
            d[k] = v


print(len([p for p in passports if p.has_fields()]))
print(len([p for p in passports if p.is_valid()]))

countries = {int(p.d.get('cid')) for p in passports if 'cid' in p.d}
print(sorted(countries))
print(len(countries))

c_to_pass = {c: [p for p in passports if p.d.get('cid') == str(c)] for c in countries}
c_to_num = {c: len(v) for c, v in c_to_pass.items()}

print(c_to_num)

for c in sorted(c_to_num, key=lambda x: c_to_num[x]):
    print(c, c_to_num[c])

num_to_countries = {}
for c, num in c_to_num.items():
    if num not in num_to_countries:
        num_to_countries[num] = [c]
    else:
        num_to_countries[num].append(c)

print(num_to_countries)
for k, v in num_to_countries.items():
    print(k, len(v))
