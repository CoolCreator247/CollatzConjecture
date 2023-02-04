import time

def collatz(num, level):
    tree = ""
    while num != 1:
        if (num % 2) == 0:
            num = num / 2
            tree += " " * level + "|\n"
            tree += " " * level + "v\n"
            tree += " " * level + str(num) + "\n"
        else:
            num = num * 3 + 1
            tree += " " * level + "|\n"
            tree += " " * level + "v\n"
            tree += " " * level + str(num) + "\n"
        level += 2
        tree += collatz(num, level)
    return tree

tree = collatz(100, 0)
print(tree)
