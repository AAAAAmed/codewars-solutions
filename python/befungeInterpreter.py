import random
def interpret(code):
    output = ""
    px = 0
    py = 0

    dx = 1
    dy = 0
    direction = "right"

    stringMode = False
    skipNext = False

    stack = []
    codeList = [[]]
    for char in list(code):
        if char != "\n":
            codeList[-1].append(char)
        else:
            codeList.append([])

    while True:
        c = codeList[py][px]

        if stringMode:
            if c == '"':
                stringMode = False
            else:
                stack.append(ord(c))

        elif skipNext:
            skipNext = False

        else:
            # Numbers
            if c.isdigit():
                stack.append(int(c))

            # Arithmetic
            elif c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(b // a)
            elif c == "%":
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    stack.append(0)
                else:
                    stack.append(b % a)

            # Logic
            elif c == "!":
                if stack.pop() == 0:
                    stack.append(1)
                else:
                    stack.append(0)
            elif c == "`":
                a = stack.pop()
                b = stack.pop()
                if b > a:
                    stack.append(1)
                else:
                    stack.append(0)

            # Movement
            elif c == "^":
                direction = "up"
            elif c == "v":
                direction = "down"
            elif c == "<":
                direction = "left"
            elif c == ">":
                direction = "right"

            elif c == "?":
                rand = random.randint(0, 3)
                directions = ["up", "down", "left", "right"]

                direction = directions[rand]
            elif c == "_":
                if stack.pop() == 0:
                    direction = "right"
                else:
                    direction = "left"
            elif c == "|":
                if stack.pop() == 0:
                    direction = "down"
                else:
                    direction = "up"

            # Strings
            elif c == '"':
                stringMode = not stringMode

            # Stack
            elif c == ":":
                if len(stack) == 0:
                    stack.append(0)
                else:
                    stack.append(stack[-1])
            elif c == "\\":
                if len(stack) == 1:
                    stack.append(0)
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a)
                    stack.append(b)
            elif c == "$":
                stack.pop()

            # Output
            elif c == ".":
                output += str(stack.pop())
            elif c == ",":
                output += chr(stack.pop())

            # Misc
            elif c == "#":
                skipNext = True
            elif c == "p":
                y = stack.pop()
                x = stack.pop()
                v = stack.pop()

                codeList[y][x] = chr(v)
            elif c == "g":
                y = stack.pop()
                x = stack.pop()
                stack.append(ord(codeList[y][x]))
            elif c == "@":
                break

        if direction == "right":
            dx = 1
            dy = 0
        elif direction == "left":
            dx = -1
            dy = 0
        elif direction == "up":
            dx = 0
            dy = -1
        else:
            dx = 0
            dy = 1

        px += dx
        py += dy

    return output

print(interpret('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^'))
print('Expected: Hello World!')
