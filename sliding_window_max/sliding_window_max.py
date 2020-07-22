'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
  

# define start and end 
    start = 0
    end = k -1
#make lsit for window numbers
    result_arr = []        


    while end <= len(nums) -1:
        max = None

        for i in range(start, end + 1):
            #if max is None, make max equal the current nums index
            if max == None:
                max = nums[i]
            #if nums current index is greater than max make max equal the current nums index
            if nums[i] > max:
                max = nums[i]
        #add the value of max to the result lsit
        result_arr.append(max)

        start += 1
        end += 1

    #return result
    return result_arr




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
