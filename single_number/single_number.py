'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Need to check an array for number that only occurs once while the rest show up twice
    # Does array actually have duplicates? use set()??
    # How to look through an array to check if there is an integer that does NOT show up twice(loop??)
    #If a single itnerger is in the array return that integer into a new array?? 
    #Else continue looping through the array until it is found


################
    #size = len(arr)
    #create a new array to find x
    not_dupl = []
    #loop through array
    for x in arr:
        #check if x should be in not_dupl[]-meaning it is a repeating number
        if x in not_dupl:
            # pop it at it's index
            not_dupl.pop(not_dupl.index(x))

        else:
            # If a non repeating number is found append it to not_dupl[]
            not_dupl.append(x)

    return not_dupl



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")