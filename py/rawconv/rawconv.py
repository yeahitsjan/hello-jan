#!/usr/bin/env python3
import sys, os
import rawpy
import imageio

arglen = len(sys.argv)

def main(args):
    if not arglen > 2:
        #show_help()
        sys.exit()

    infile = sys.argv[1] ## inputfile is always first arg
    outfile = sys.argv[2] ## outfile always second
    with rawpy.imread(infile) as raw:
        rgb = raw.postprocess()
    imageio.imsave(outfile, rgb)

if __name__ == '__main__':
    main(sys.argv)