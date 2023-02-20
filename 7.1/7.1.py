template = """
Prefix              {}
AD/Metric           {}  
Next-Hop            {} 
Last update         {}
Outbound Interface  {}"""
with open("ospf.txt") as f:
    for ospf_route in f:
        ospf_route = ospf_route[1:]
        ospf_route = ospf_route.replace(',','').replace("via","").strip()
        item_list = ospf_route.split()
        print(template.format((item_list[0]),(item_list[1].strip("[]")),(item_list[2]),(item_list[3]),(item_list[4])))