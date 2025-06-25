import re

def compress_ipv6(ipv6_address,debug=False):
    if len(ipv6_address) != 39:
        raise Exception("Please input a valid IPv6 address")
    
    max = 0
    count = 0
    end_index = float("-inf")
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
    
    # Convert the end_index to an r, to allow for a small hack later....
    if end_index > float("-inf"):
        section_list[end_index] = "r"
    
    # Remove list elements so can format output correctly with :: substituting!
    
    if max >=2:
        del section_list[(end_index-(max-1)):(end_index)]
                    
    # Convert result to lowercase to improve readability, the "r" acts a placeholder for where the :: need to be.
    # Using regex for replacement as allows for instances where the "r" placeholder appears in first position to no ":" before.
    result = ":".join(section_list).lower()
    result = re.sub(r"(\:*r\:*)","::",result)
   
    # Debugging prints below, to help troubleshoot variables
    if debug:
        print(f"section_list Output: {section_list}")
        print(f"Result: {result}")
        print(f"0's Count:{max}")
        print(f"Range:{end_index-(max-1)}-{end_index}")
    
    return result

def expand_ipv6(ipv6_address,debug=False):
    section_list = ipv6_address.split(":")
    if "" in section_list:
        i_p = section_list.index("")
        
    for i in range(0,(len(section_list))):
        # if section_list[i] == "":
        #     section_list.insert(i,"0000")
        if len(section_list[i]) != 4:
            miss_char = 4 - len(section_list[i])
            section_list[i] = (miss_char*"0")+section_list[i]
    
    if len(section_list) !=8:
        to_insert = 8 - len(section_list)
        while to_insert !=0:
            section_list.insert(i_p,"0000")
            to_insert -=1
    result = ":".join(section_list).lower()

    # Debugging prints below, to help troubleshoot variables
    if debug:
        print(f"section_list Output: {section_list}")
        print(f"Result: {result}")
        # print(f"0's Count:{max}")
        # print(f"Range:{end_index-(max-1)}-{end_index}")
    
    return result