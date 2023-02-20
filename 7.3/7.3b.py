user_vlan = input("Enter VLAN number: ")

with open("CAM_table.txt", "r") as table:
    for index in table:
        line = index.split()
        if line and line[0].isdigit() and line[0] == user_vlan:
            vlan, mac, _, intf = line
            print(f"{vlan:9}{mac:20}{intf}")