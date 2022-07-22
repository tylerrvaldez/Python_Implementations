#  File: Cipher.py

#  Description: Read in strings from standard in and encrypt and decrypt strings P and Q making sure to utilize 2-D lists.

#  Student Name: Tyler Valdez

#  Student UT EID: trv359

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 9/08/2021

#  Date Last Modified: 09/13/2021

import math
import sys


# Finds side length of string by finding the smallest square number greater than or equal to the length of string.
def pad_string(s):
    side_length = math.ceil(len(s) ** 0.5)
    while len(s) < side_length ** 2:
        s += "*"
    return s

# Creates 2D matrix by using the side length to create even rows and columns.
def make_square(s):
    side_length = math.ceil(len(s) ** 0.5)
    padded_string = pad_string(s)
    outer_list = []
    for i in range(len(padded_string)):
        if i % side_length == 0:
            # create substring of i.
            substring = padded_string[i:i + side_length]
            # converts string to a list of characters
            outer_list.append(list(substring))  
    return outer_list


def rotate_clockwise(square):
    # rotates the matrix 90 degrees clockwise.
    side_length = len(square[0])
    for i in range(side_length // 2):
        for j in range(i, side_length - i - 1):
            # keep track of current cell.
            temp = square[i][j]
            # rotate from right to top cell.
            square[i][j] = square[side_length - 1 - j][i]
            # move from bottom to right cell.
            square[side_length - 1 - j][i] = square[side_length - 1 - i][side_length - 1 - j]
            # move from left to bottom cell.
            square[side_length - 1 - i][side_length - 1 - j] = square[j][side_length - 1 - i]
            # set to next cell
            square[j][side_length - 1 - i] = temp
    return square


def rotate_counter_clockwise(square):
    side_length = len(square[0])
    # rotate matrix 90 degrees counter clockwise to decrypt the string.
    for x in range(0, int(side_length / 2)):
        # consider each element in the group in relation to size of string.
        for y in range(x, side_length - x - 1):
            # keeps track of current cell
            temp = square[x][y]
            # rotate from the right to the top cell
            square[x][y] = square[y][side_length - 1 - x]
            # move from bottom to right cell
            square[y][side_length - 1 - x] = square[side_length - 1 - x][side_length - 1 - y]
            # move from left to bottom cell.
            square[side_length - 1 - x][side_length - 1 - y] = square[side_length - 1 - y][x]
            # set to next cell
            square[side_length - 1 - y][x] = temp
    return square

# Input: strng is a string of 100 or less of upper case, lower case,and digits
# Output: function returns an encrypted string
def encrypt(strng):
    square = make_square(strng)
    square = rotate_clockwise(square)
    encryptstr = (''.join(ele for sub in square for ele in sub)).replace("*", "")
    return encryptstr

# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string
def decrypt(strng):
    str_list = list(strng)
    # creates a temporary string that replaces each element in strng with a random sign.
    dummy_string = "".join(["$" for letter in str_list])
    # rotates the temporary string clockwise to figure out the padding of the 2d matrix we will use for decryption.
    dummy_rotated_square = rotate_clockwise(make_square(dummy_string))
    dummy_rotated_padded_string = "".join(["".join(x) for x in dummy_rotated_square])
    padded_string = ""
    # the for loop will go through the index of the temporary padded list and add either an asterick or the letter into the padded list that we will use to turn counter clockwise for decrypting.
    for dummy_index in range(len(dummy_rotated_padded_string)):
        if dummy_rotated_padded_string[dummy_index] == "*":
            padded_string += "*"
        else:
            padded_string += str_list.pop(0)  # returns the first letter and removes it from the string
    square = make_square(padded_string)
    square = rotate_counter_clockwise(square)
    decryptstr = ''.join(ele for sub in square for ele in sub).replace("*", "")
    return decryptstr

def main():
    # read the two strings P and Q from standard input
    P = str(sys.stdin.readline().strip())
    Q = str(sys.stdin.readline().strip())

    # encrypt the string P
    enc = encrypt(P)
    # decrypt the string Q
    dec = decrypt(Q)

    # print the encrypted string of P and the
    # decrypted string of Q to standard out
    print(enc)
    print(dec)


if __name__ == "__main__":
    main()
