opening = ["(", "{", "["]
closing = [")", "}", "]"]

def is_match(s):

    stack = []

    for letter in s:
        if letter in opening:
            stack.append(letter)
        elif letter in closing:
            if len(stack) > 0:
                if closing.index(letter) == opening.index(stack[-1]):
                    stack.pop()
            else:
                return "Unbalanced"
    
    if len(stack) == 0:
        return "Balanced"
    else:
