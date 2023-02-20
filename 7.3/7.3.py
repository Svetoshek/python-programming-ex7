with open("CAM_table.txt") as table:
    for index in table:
        line = index.split()
        if line and line[0].isdigit():
            vlan, mac, _, interface = line
            print(f"{vlan:9}{mac:20}{interface}")