# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    global opening_brackets_stack
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                opening_brackets_stack[-1] = opening_brackets_stack[-1]._replace(position=i+1)
                return 0
            else:
                opening_brackets_stack.pop()
            

def main():
    text = input()
    print(text)
    if "I\n" in text:
        text = text[2::]
    print(text)
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if not opening_brackets_stack:
        print("Success")
    else:
        print(opening_brackets_stack[-1].position)


if __name__ == "__main__":
    main()
