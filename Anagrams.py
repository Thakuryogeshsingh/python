from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)

    return dfdict.values()

word=["ram", "banana","mar","bat","ball","name"]
print(group_anagrams(word))

