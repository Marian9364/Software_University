version = input().split(".")
new_list = "".join(version)
new_list = int(new_list)
next_version = new_list + 1
next_version = str(next_version)
next_version_list = []
for num in next_version:
    next_version_list.append(num)

print(".".join(next_version_list))
