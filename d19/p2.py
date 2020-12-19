#!/usr/bin/python3
import re

with open('input') as f:
    lines = [x.strip() for x in f.readlines()]


# lines = """0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b""".splitlines()
# 
# lines = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
# 
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb""".splitlines()

TEST = False
if TEST:
    lines = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".splitlines()


class Rule:
    def __init__(self, num, rule_str):
        self.num = num
        self.rule_str = rule_str
        self.solved = False
        self.valid = []     # List of strs that are valid
        self.unsolved = []  # List of list of nums
        self.recursive = self.num in self.rule_str

        if '"' in rule_str:
            self.valid = [rule_str[1]]
            self.solved = True
        elif '|' in rule_str:
            r1, r2 = rule_str.split(" | ")
            self.unsolved = [r1.split(), r2.split()]
        else:
            self.unsolved = [rule_str.split()]

    def __repr__(self):
        return f"<Rule: {self.rule_str}>"

    def solve(self, subrule, all_rules):
        if subrule not in self.unsolved:
            return

        subrule_strs = [all_rules[num].valid for num in subrule]
        subrule_solved = combine_options(subrule_strs)
        
        self.unsolved.remove(subrule)
        self.valid.extend(subrule_solved)

        if len(self.unsolved) == 0:
            self.solved = True


rules = {}
messages = []
DORULE = True
for line in lines:
    if DORULE:
        if not line:
            DORULE = False
            continue
        num, rule_str = line.split(": ")
        rules[num] = Rule(num, rule_str)
    else:
        messages.append(line)


#8: 42 | 42 8
#11: 42 31 | 42 11 31


rules['8'] = Rule("8", "42 | 42 8")
rules['11'] = Rule("11", "42 31 | 42 11 31")


def combine_options(options):
    """
    Takes a list of list of strs and returns the list of
    combinations
    in -> [['a']]
    out -> ['a']

    in -> [['a'], ['b']]
    out -> ['ab']

    in -> [['a', 'b'], ['b']
    out -> ['ab', 'bb']
    """
    solns = [""]
    for option_set in options:
        option_strs = []
        for s in solns:
            for op in option_set:
                option_strs.append(s + op)
        solns = option_strs
    return solns

# Make '0' recursive so this will end
rules['0'].recursive = True
while not all(r.solved or r.recursive for r in rules.values()):
    for num, rule in rules.items():
        if rule.solved:
            continue

        for subrule in rule.unsolved:
            if all(rules[num].solved for num in subrule):
                rule.solve(subrule, rules)



print(rules['42'].valid)
print(rules['31'].valid)


#8: 42 | 42 8
# Means match 42 1 or more times
#11: 42 31 | 42 11 31
# means match 42 x times then match 31 x times
# So 0: 8 11 means:
# match 42 2 or more times then match 31 1 or more times - but less that 42


r42 = "|".join(rules['42'].valid)
r31 = "|".join(rules['31'].valid)


n=0

print(f"^({r42})({r42})+({r31})+$")
for test in messages:
    if re.match(f"^({r42})+({r42}){{1}}({r31}){{1}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{2}}({r31}){{2}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{3}}({r31}){{3}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{4}}({r31}){{4}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{5}}({r31}){{5}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{6}}({r31}){{6}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{7}}({r31}){{7}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{8}}({r31}){{8}}$", test):
        n += 1
    elif re.match(f"^({r42})+({r42}){{9}}({r31}){{9}}$", test):
        n += 1

print(n)
