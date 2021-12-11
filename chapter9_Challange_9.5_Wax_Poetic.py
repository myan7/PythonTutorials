import random

Nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
Verbs = ["kicks", "jingles", "bounces", "slurps", "meows",
"explodes", "curdles"]
Adjectives = ["furry", "balding", "incredulous", "fragrant",
"exuberant", "glistening"]
Prepositions = ["against", "after", "into", "beneath", "upon",
"for", "in", "like", "over", "within"]
Adverbs = ["curiously", "extravagantly", "tantalizingly",
"furiously", "sensuously"]

noun1 = random.choice(Nouns)
adj1 = random.choice(Adjectives)
verb1 = random.choice(Verbs)
prep1 = random.choice(Prepositions)
adverb1 = random.choice(Adverbs)
noun2 = random.choice(Nouns)
verb2 = random.choice(Verbs)
adj2 = random.choice(Adjectives)
prep2 = random.choice(Prepositions)
adj3 = random.choice(Adjectives)
noun3 = random.choice(Nouns)
verb3 = random.choice(Verbs)

first = 'An' if adj1[0] in ('a','e','i','o','u') else 'A'

print(f"""
{first} {adj1} {noun1}

{first} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}
{adverb1}, the {noun1} {verb2}
the {noun2} {verb3} {prep2} a {adj3} {noun3}
""")
