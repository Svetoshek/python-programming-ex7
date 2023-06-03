ignore = ["duplex", "alias", "Current configuration"]

with open('config_sw1.txt') as f:
    for line in f:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            print(line.rstrip())
