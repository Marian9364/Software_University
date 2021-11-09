import re
pattern = r"(www.[a-zA-Z0-9\-]+(\.[a-z]+){1,})"
ll = []
data = input()
while len(data) > 0:
    matches = re.finditer(pattern, data)
    for match in matches:
        print(match.group())
    data = input()
