'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # shift 0's to the left side of the array
    # return the altered array
    # if there are no 0s print the array
    # create a variable to hold the non-zeroes
    # Loop - for x in the range of the length of the array
        # x holds the zeroes in the equation, so if x doesnt equal zero and moved DOES equal zero
        # the array's order becomes the moved nonzero number to the left, and the zero to the right for the entire array
        # if moved didn't equal zero, move the index to check the next one


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")