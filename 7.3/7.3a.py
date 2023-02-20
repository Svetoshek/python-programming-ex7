mac_table = []

with open("CAM_table.txt", "r") as table:
    for index in table:
        line = index.split()
        if line and line[0].isdigit():
            vlan, mac, _, intf = line
            mac_table.append([int(vlan), mac, intf])

for vlan, mac, intf in sorted(mac_table):
    print(f"{vlan:<9}{mac:20}{intf}")