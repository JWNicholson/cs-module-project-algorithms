'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # Loop through the array -  on each index remove it and multiply the rest of the numbers in the array
    # return that number to a new array
    # ?? multiply the right side of the array and the left side of the array -combine those two into a final integer ??

    right = [0] * len(arr)
    right[-1] == arr[-1]#end of array

    for i in range(1,len(arr)):
        right[len(arr)-i-1] = right[len(arr)-i] * arr[len(-i-1)]
        out = [0] * len(arr)
        prefix = 1
        current_index = 0
        while current_index < len(out)-1:
            out[current_index] = prefix * rihgt[current_index + 1]
            prefix *= arr[current_index]
            current_index  +=1
            out[-1]= prefix
        
        return out


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
