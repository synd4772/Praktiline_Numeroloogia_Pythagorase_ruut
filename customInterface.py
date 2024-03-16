def warning(text, max_length = None, percent = 0.2, after = None, temp_warning_text = "WARNING!!!"):
    text_list = []
    if max_length is None:
        max_length = len(text) - 10
        if len(text) > 60:
            max_length -= 60

    if max_length < len(text):
        temp_text_list = text.split(" ")
        summa = 0
        temp_list = list()
        for letter in temp_text_list:
            summa += len(letter)
            temp_list.append(letter)
            if summa > (max_length - max_length * percent):
                text_list.append(temp_list.copy())
                temp_list.clear()
                summa = 0
    warning_text = ""
    for i in range(0,100):
        if max_length + max_length * percent > len(warning_text) - (len(warning_text) * percent):
            warning_text += temp_warning_text
        else:
            break

    line = f"+{'-' * (len(warning_text) + 2)}+"
    print(line)
    print(f"| {warning_text} |")
    print(f"+{'=' * (len(warning_text) + 2)}+")
    if len(text_list) > 1:
        for i in text_list:
            temp_text = ' '.join(i)
            temp_length = len(' '.join(i))
            print(f"| {temp_text}{' ' * (len(line) - (temp_length + 3))}|")
    else:
        print(f"| {text}{' ' * (len(line) - (len(text) + 3))}|")
    print(line)

    if after is not None:
        print(after)
