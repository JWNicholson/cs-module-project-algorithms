'''
Input: an integer
Returns: an integer
'''
#def eating_cookies(n):
    # Your code here
# def eating_cookies(n, cookie_jar=None):
    
#     if cookie_jar == None:
#         cookie_jar = [0] * (n + 1)

#     if n <= 1:
#         cookie_jar[n] =1

#     elif n == 2:
#         cookie_jar[n] = 2

#     elif cookie_jar[n] == 0:
#         cookie_jar[n] = eating_cookies(n - 1, cookie_jar) + eating_cookies(n - 2, cookie_jar) + eating_cookies(n - 3, cookie_jar)

#     return cookie_jar[n]


def eating_cookies(n, cache=None):
    total = 0
    if n == 0:
        return 1
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
       
            cache = {i:0 for i in range(n+1)}
        for start_with in range(1,3+1):
            if n >= start_with:
                total += eating_cookies(n - start_with, cache)
        cache[n] = total
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
