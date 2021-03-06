#!/bin/python
import convert
import sys
from PIL import Image

def main (path,offx=0, offy=0):
    print('\n'.join(generateFrame(path,offx,offy)))

def generateFrame(path,offx,offy):
    return convert.main(Image.open(path).convert('RGBA'),offx,offy)
if __name__ == '__main__' :
		if len(sys.argv) == 4:
			main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
		main(sys.argv[1])
