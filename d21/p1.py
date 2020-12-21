#!/usr/bin/python3
with open('input') as f:
    lines = [x.strip() for x in f.readlines()]

# lines = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()


allergen_possibles = {}
all_ingredients = set()
ingredient_count = {}

for line in lines:
    ingredients, allergens = line[:-1].split(" (contains ")
    ingredients = ingredients.split()
    allergens = allergens.split(", ")
    ing_set = set(ingredients)
    all_ingredients = all_ingredients.union(ing_set)

    for i in ingredients:
        if i in ingredient_count:
            ingredient_count[i] += 1
        else:
            ingredient_count[i] = 1

    for a in allergens:
        if a in allergen_possibles:
            allergen_possibles[a] = allergen_possibles[a].intersection(ing_set)
        else:
            allergen_possibles[a] = ing_set

bad = set()
for a, possible in allergen_possibles.items():
    bad = bad.union(possible)

good_ingredients = [i for i in all_ingredients if i not in bad]

print(sum(v for k, v in ingredient_count.items() if k in good_ingredients))

allergen_definites = {}

while len(allergen_definites) != len(allergen_possibles):
    for a, pos in allergen_possibles.items():
        if a in allergen_definites:
            continue
        if len(pos) == 1:
            i = list(pos)[0]
            allergen_definites[a] = i
            for k in allergen_possibles:
                if k != a:
                    try:
                        allergen_possibles[k].remove(i)
                    except:
                        pass

print(",".join([allergen_definites[a] for a in sorted(allergen_definites)]))
