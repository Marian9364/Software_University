import re
pattern = r"(?<=\s_)[a-zA-Z0-9]+\b"

text = input()

matches = re.findall(pattern, text)



print(",".join(matches))
