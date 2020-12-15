# Dictionary task - collecting likes and comments of users and manipulating the data

dict_ = {}
command = input()

while command != "Log out":
    data = command.split(": ")
    to_do = data[0]
    username = data[1]
    if to_do == "New follower":
        if username not in dict_:
            dict_[username] = {"likes": 0, "comments": 0}
    elif to_do == "Like":
        count = int(data[2])
        if username not in dict_:
            dict_[username] = {"likes": count, "comments": 0}
        elif username in dict_:
            dict_[username]["likes"] += count
    elif to_do == "Comment":
        if username not in dict_:
            dict_[username] = {"likes": 0, "comments": 1}
        elif username in dict_:
            dict_[username]["comments"] += 1
    elif to_do == "Blocked":
        if username in dict_:
            del dict_[username]
        elif username not in dict_:
            print(f"{username} doesn't exist.")
    command = input()

followers_count = len(dict_)
print(f"{followers_count} followers")

for key, value in dict_.items():
    sum_ = (value['comments'] + value['likes'])
    dict_[key]["sum"] = sum_

ordered_dict = sorted(dict_.items(), key=lambda x: (-x[1]["sum"], x[0]))
for key, value in ordered_dict:
    print(f"{key}: {value['sum']}")





