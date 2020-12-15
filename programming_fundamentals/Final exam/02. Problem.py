# RegEx task

import re
pattern = r"![A-Z][a-z]{2,}!:\[[a-zA-Z]{8,}\]"
dict_to_work = {}
list_of_ascii_nums = []
n = int(input())
for _ in range(n):
    msg = input()
    match = re.match(pattern, msg)
    if match:
        word_to_iter = match.group()
        command_and_msg = word_to_iter.split(":")
        command = command_and_msg[0]
        command = command.replace("!", "")
        msg_to_ascii = command_and_msg[1]
        for char in msg_to_ascii:
            if char.isalpha():
                list_of_ascii_nums.append(str(ord(char)))
        print(f"{command}: {' '.join(list_of_ascii_nums)}")
        match = False
    else:
        print("The message is invalid")

