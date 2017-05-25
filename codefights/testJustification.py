
def text_justification(words, l):
    size = 0
    lines = []
    line = []
    for word in words:
        if size + len(word) + 1 < l:
            size += len(word) + 1
            line.append(word)
        else:
            lines.append(line)
            size = len(word)
            if word == words[-1]:
                lines.append([word])
            else:
                line = [word]

    for items in lines:
        spaces = len(items) - 1
        total_length = len(" ".join(items))
        remaining_length = l - total_length
        print(remaining_length)

    return lines

words = ["This", "is", "an", "example", "of", "text", "justification."]
l = 16
print(text_justification(words, l))

