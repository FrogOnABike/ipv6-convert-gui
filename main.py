from sys import argv
from functions import compress_ipv6, expand_ipv6
from classes import *

def main():
    debug = False
    if len(argv) == 1:
        print ('Usage: "main.py <ipv6 address>" or "main.py --gui" to launch GUI version.')
        exit(1)
    else:
        address = argv[1]
    
    if "--debug" in argv:
        debug = True
        
    # if "--expand" in argv:
    #     expand_ipv6(address)
    
    if "--gui" in argv:
        Window(200,100)
        
    if len(address) != 39:
        print(expand_ipv6(address,debug))
    else:
        print(compress_ipv6(address,debug))
    
if __name__ == "__main__":
    main()
    
    