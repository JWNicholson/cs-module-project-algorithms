'''
Input: an integer
Returns: an integer
'''
#def eating_cookies(n):
    # Your code here
def eating_cookies(n, cookie_jar=None):
    
    if cookie_jar == None:
        cookie_jar = [0] * (n + 1)

    if n <= 1:
        cookie_jar[n] =1

    elif n == 2:
        cookie_jar[n] = 2

    elif cookie_jar[n] == 0:
        cookie_jar[n] = eating_cookies(n - 1, cookie_jar) + eating_cookies(n - 2, cookie_jar) + eating_cookies(n - 3, cookie_jar)

    return cookie_jar[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
