#String manipulations

word = input()
ascii_sum = 0
command = input()
while command != "Finish":
    data = command.split()
    to_do = data[0]
    if to_do == "Replace":
        current_char = data[1]
        new_char = data[2]
        word = word.replace(current_char, new_char)
        print(word)
    elif to_do == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(word)) and end_index in range(len(word)):
            word = word[:start_index] + word[end_index + 1:]
            print(word)
        else:
            print("Invalid indices!")
    elif to_do == "Make":
        if data[1] == "Upper":
            word = word.upper()
        elif data[1] == "Lower":
            word = word.lower()
        print(word)
    elif to_do == "Check":
        string = data[1]
        if string in word:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif to_do == "Sum":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(word)) and end_index in range(len(word)):
            substring = word[start_index:end_index + 1]
            for char in substring:
                ascii_sum += ord(char)
            print(ascii_sum)
        else:
            print("Invalid indices!")
    command = input()
