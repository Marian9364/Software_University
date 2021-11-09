import re
pattern = r"\d+"
matches_filled = []
text = input()
while text:
    matches = re.findall(pattern, text)
    matches_filled.extend(matches)

    text = input()

print(*matches_filled, sep=" ")
