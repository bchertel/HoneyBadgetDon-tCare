#!/usr/bin/ python
import hashlib


def md5_hash(string):
    return hashlib.md5(string).hexdigest()

def print_array(arr):
    stringOut = flag1 + ''.join('{0}'.format(element) for element in arr)
    file.write(stringOut + "\t" + md5_hash(stringOut) + "\n")

def inc_cell(arr, position, minimum, maximum):
    for i in range(minimum, maximum):
        arr[position] = i
        print_array(arr)

def inc_array(arr, current_position, minimum, maximum):

    if current_position == array_max_position:
        inc_cell(arr, current_position, minimum, maximum)

    else:
        for i in range(minimum, maximum):
            arr[current_position] = i
            inc_array(arr, (current_position + 1), minimum, maximum)

if __name__ == '__main__':
    file = open("data.txt", "w+")

    print"Enter the first half of the flag: "
    flag1 = raw_input()

    print"Enter how large of an array you would like: "
    array_size = int(raw_input())

    array_max_position = array_size - 1
    min_range = 0
    max_range = 10
    array = bytearray(array_size)
    inc_array(array, 0, min_range, max_range)

    file.close()
    print"Brute.py Finished"
