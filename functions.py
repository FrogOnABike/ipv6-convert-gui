def compress_ipv6(ipv6_address):
    max = 0
    current = 0
    end_index = 0
    section_list = ipv6_address.split(":")
    
    # Initial pass to replace all groups of "0000" with "0" and remove leading 0's in others
    for i in range(len(section_list)):
        if section_list[i] == "0000":
            section_list[i] = "0"
        else:
            section_list[i] = section_list[i].lstrip("0")
    
    # Locate longest section of 0's to remove - Keep a track of no. of consecutive 0 blocks and check against current longest (max)
    # If higher then update max and end_index. Can then subtract max-1 from end_index to work out range to remove.
    for i in range(len(section_list)):
        if section_list[i] == "0":
            count += 1
            if count > max:
                max = count
                end_index = i
        else:
            count = 0
    
    # Convert the end_index 0 to an r, to allow for a small hack later....
    section_list[end_index] = "r"
    print(f"Output 1: {section_list}")
    
    # Remove list elements so can format output correctly with :: substituting!
    
    if max >=2:
        del section_list[(end_index-(max-1)):(end_index)]
        # for r in range(end_index-(max-1),(end_index)):
        #     section_list.pop(r)
                    
    # Convert result to lowercase to improve readability
    result = ":".join(section_list).lower()
    print(f"Output: {section_list}")
    # Now we have the output string, the r acts a placeholder for where the :: need to be :)
    print(f"Result: {result.replace(":r:","::")}")
    print(f"0's Count:{max}")
    print(f"Range:{end_index-(max-1)}-{end_index}")
    