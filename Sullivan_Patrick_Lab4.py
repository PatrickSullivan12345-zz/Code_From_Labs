#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      pps7
#
# Created:     06/02/2018
# Copyright:   (c) pps7 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def q4(word, char):

    num = 0

    for i in word:
        if i == char:
            num += 1
    return num

if __name__ == '__main__':
    main()

    word = "goodbye"
    char = "o"
    print q4(word,char)

    """
def q4(word, char):
    num = 0
    for i in word:
        if i == char:
            num + 1
    return num

if __name__ == '__main__':
    main()
    w = "goodbye"
    char = "o"
    print q4(w,char)
    """