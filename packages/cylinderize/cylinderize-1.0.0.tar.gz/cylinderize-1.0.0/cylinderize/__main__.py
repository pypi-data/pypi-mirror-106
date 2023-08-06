from . import cylinderize
from sys import argv
def main(): cylinderize(open(argv[1]).read())
if __name__ == "__main__": main()