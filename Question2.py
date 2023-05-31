from collections import Counter
def valid_string(string):
    # First let's use the Counter Function to count the occurance of each letter of the string
    letter_occur = dict(Counter(string))
    max_occur = max(list(letter_occur.values()))
    min_occur = min(list(letter_occur.values()))
    # Now, let's see if the highest occurance of a letter is the same as the lowest occurance of a letter
    # If it is true then It means that every letter occur the same number of time
    if max_occur == min_occur:
        return "Yes" 
    # Now, if the program failed to enter the first if block, then let's try to see if the difference between
    # Highest occurance and lowest occurance of a letter is 1. If its true, we will enter this if block.
    elif max_occur - min_occur == 1:
        # Now, we have to check if there are more than 1 letters than have the same occurance as max_occur. If there are more, then return No.
        # Else, return yes
        if list(letter_occur.values()).count(max_occur) == 1:
            return "Yes"
        else:
            return "No"
    else: 
        return "No"


print(valid_string("abc")) # Test case 1


print(valid_string("aabcc")) # Test case 2
#Explanation: So in the above string, we can see that there are 2 occurance of a and c. it will look like {"a": 2, "b": 1, "c": 2}. As we can see, 
# although reducing the occurance of a and c by 1, we can get all 3 same occurance, but we can only do it for 1 letter. So, this string is not valid. 

print(valid_string("aabccc")) # Test Case 3
#Explanation: So in this string, we can see that there are 2 occurance of a, and 3 occurance of c. So, this string is straight up invalid.