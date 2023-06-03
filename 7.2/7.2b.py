ignore = ["duplex", "alias", "configuration"]

src_file, dst_file = "config_sw1.txt", "config_sw1_cleared.txt"

with open(src_file) as src, open(dst_file, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)
