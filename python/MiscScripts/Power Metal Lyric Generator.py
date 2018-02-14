import random

verbs = [
    "galloping",
    "crying",
    "enlightening",
    "darkening",
    "fly",
    "rise",
    "reflects",
    "climb",
    "burn",
    "redeem",
    "power",
    "guide",
    "standing",
    "blazing",
    "reaching",
    "searching"
];
adverbs = [
    "triumphantly",
    "quickly",
    "eternally",
    "brightly",
    "vengefully",
    "courageously",
    "defiantly",
    "gracefully",
    "solemnly",
    "viciously",
    "sorrowfully",
    "bravely",
    "mysteriously",
    "violently",
    "frantically",
    "wildly"
];
prepositions = [
    "through",
    "into",
    "above",
    "beneath",
    "beyond",
    "amongst",
    "below",
    "under",
    "in",
    "against",
    "within",
    "inside",
    "before",
    "outside"
];
adjectives = [
    "snowy",
    "shining",
    "glowing",
    "ancient",
    "rising",
    "crystal",
    "fantastical",
    "soulful",
    "aggressive",
    "courageous",
    "defiant",
    "bloody",
    "cloudy",
    "graceful",
    "misty",
    "icy"
];
nouns = [
    "moonlight",
    "darkness",
    "defendors",
    "wings",
    "light",
    "fields",
    "destiny",
    "sun",
    "heavens",
    "souls",
    "sunlight",
    "battle cry",
    "night",
    "skies",
    "dream",
    "clouds"
];
nouns2 = [
    "path",
    "ice",
    "mountain",
    "plains",
    "hearts",
    "stars",
    "fire",
    "lands",
    "abyss"
]
def randomWord(array):
    return array[random.randrange(0,len(array))]

for i in range(4):
    string = randomWord(verbs) + ' ' + randomWord(adverbs) + ' ' + randomWord(prepositions) + ' ' + randomWord(adjectives) + ' ' + randomWord(nouns) + ' ' + randomWord(nouns2) + '.'
    print(string[0].toUpper() + string[1:])
