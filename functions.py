def compress_ipv6(ipv6_address):
    section_list = ipv6_address.split(":")
    for i in range(len(section_list)):
        if section_list[i].startswith("0"):
            section_list[i]=section_list[i].replace("0","",3)
        elif section_list[i].startswith("00"):
            section_list[i]=section_list[i].replace("0","",2)
        elif section_list[i].startswith("000"):
            section_list[i]=section_list[i].replace("0","",1)

    print(F"Output: {section_list}")