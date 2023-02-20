from sys import argv
with open(argv[1]) as f:
    for string in f:
        if string[0] != "!":
            print(string.rstrip())