'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # shift 0's to the end of the array
    # return the altered array

    # if there are no 0s print the array
    
    # create a variable to hold the non-zeroes
    moved = 0
    # Loop - for x in the range of the length of the array
    for x in range(len(arr)):
        # x holds the zeroes in the equation, so if x doesnt equal zero and moved DOES equal zero
        if arr[x] != 0 and arr[moved] == 0:
            # the array's order gets swapped
            arr[x], arr[moved] = arr[moved], arr[x]

        if arr[moved] !=0:
            # if moved didn't equal zero, move the index to check the next one
            moved +=1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")