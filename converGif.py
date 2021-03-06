#!/bin/python
import convert
import sys
from subprocess import call
from PIL import Image
import os
def main (path,offx=0, offy=0,stdout=False):
    call(['mkdir','tmpdir'])
    cmdstr = 'tmpdir/out%d.png'
    call(["convert",path,'-coalesce',cmdstr])
    framelist = []
    for filename in sorted(os.listdir('tmpdir')):
        framelist.append(convert.main(Image.open('tmpdir/'+str(filename)).convert('RGBA'),offx,offy))
    call(['rm','-R','tmpdir'])
    if stdout:
        print('\n'.join('\n'.join(l) for l in framelist))    
    return framelist

if __name__ == '__main__' :
		if len(sys.argv) == 4:
			main(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
		main(sys.argv[1])
