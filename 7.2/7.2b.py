ignore = ["duplex", "alias", "configuration"]
from sys import argv
with open(argv[1]) as f, open(argv[2],"w") as output_file:
    for string in f:
        if string[0] != "!":
            continue
        contain = False
        for i in ignore:
            if i in string:
                contain = True
        if not contain:
            output_file.write(string)