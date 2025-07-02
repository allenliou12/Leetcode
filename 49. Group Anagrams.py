# 49. Group Anagrams
# from collections import defaultdict

# # Input:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# key = {}
# for i in strs:
#     key[i] = tuple(sorted(i))

# print(key)
# anagrams = defaultdict(list)
# for word in strs:
#     key = tuple(sorted(word))
#     anagrams[key].append(word)

# print(list(anagrams.values()))
