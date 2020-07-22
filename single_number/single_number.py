'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Need to check an array for number that only occurs once while the rest show up twice
    # How to look through an array to check if there is an integer that does NOT show up twice(loop??)
    #If a single itnerger is in the array return that integer into a new array??
    #Else continue looping through the array until it is found

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")