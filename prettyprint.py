#!/usr/bin/env python

def read_file_printpretty(filename):
    f = open(filename,'r')
    twoLines = ""
    numLines = 0

    for line in f:
        numLines += 1
        if ( numLines % 2) != 0:
            twoLines = twoLines + line.strip() + "            "
        else:
            twoLines = twoLines + line.strip()
            print(twoLines)
            twoLines = ""

def main():

    read_file_printpretty("test")


if __name__ == "__main__":
    main()
