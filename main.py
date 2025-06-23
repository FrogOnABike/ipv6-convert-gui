from sys import argv
from functions import compress_ipv6

def main():
    if len(argv) == 1:
        print ('Usage: "main.py <ipv6 address>"')
        exit(1)
    else:
        address = argv[1]

    if len(address) != 39:
        print("Invalid address input!")
    else:
        compress_ipv6(address)
if __name__ == "__main__":
    main()
    
    