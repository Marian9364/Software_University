import re

text = input().lower()
word_to_find = input().lower()
pattern = fr"\b{word_to_find}\b"




matches = re.findall(pattern, text)



print(len(matches))
