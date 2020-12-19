#!/usr/bin/python3
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

class Rule:
    def __init__(self, rule_str):
        self.rule_str = rule_str
        self.solved = False
        self.valid = []     # List of strs that are valid
        self.unsolved = []  # List of list of nums

        if '"' in rule_str:
            self.valid = [rule_str[1]]
            self.solved = True
        elif '|' in rule_str:
            r1, r2 = rule_str.split(" | ")
            self.unsolved = [r1.split(), r2.split()]
        else:
            self.unsolved = [rule_str.split()]

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
        num, rule = line.split(": ")
        rules[num] = Rule(rule)
    else:
        messages.append(line)

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


while not all(r.solved for r in rules.values()):
    for num, rule in rules.items():
        if rule.solved:
            continue

        for subrule in rule.unsolved:
            if all(rules[num].solved for num in subrule):
                rule.solve(subrule, rules)


R0 = set(rules['0'].valid)
n=0
for test in messages:
    if test in R0:
        n += 1
print(n)
