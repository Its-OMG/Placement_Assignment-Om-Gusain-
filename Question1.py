from collections import Counter

def count_words(string):
    # First We will split the string into words and Convert it into a list
    list_string = string.split()
    # Now we will use the Counter method to count the occurance of each word in the list. It will give us a Counter Object. I will turn it into dictionary.
    words = dict(Counter(list_string))
    #Now, let's find the highest occuring word using the max function on the list of values of the dictionary. 
    max_count = max(sorted(list(words.values())))
    # print(words)   # Showing Number of Occurance Of each word 
    # print(max_count)  # Print The Maximum number of Occurance
    if list(words.values()).count(max_count) == 1:
        word = list(words.keys())[list(words.values()).index(max_count)]  # Getting the word that is occuring the most
        return len(word) # Returning the Length of Highest Occuring Word
    elif list(words.values()).count(max_count)>1:
        # Program Will Only enter this Elif block if there are more than 1 word occuring the most frequently. 
        mfw = [i for i in list(words.keys()) if words.get(i)==max_count] # This will get a list of all the Words that are have the highest Occuring Frequency.
        max_val = max(mfw, key=lambda x: len(x)) # This will give us the word with the highest length
        return len(max_val) # Returning the word that Occured the most and has the biggest in length

print(count_words("write write write all the number from from from 1 to 100"))  # Test Case 1


print(count_words("Hello Hello Hello Hello how how are you doing today today today today")) # Test Case 2
# Explanation: As we can see in the string, [Hello, today] were occuring 4 times each. But at the same time, each of those words
# had the length 5, so the first word matching having the highest length was selected and the length 5 was returned.

print(count_words("Hello Bro! How How are you today?")) # Test case 3
#Explanation: In the above string, only the word 'How' was occuring twice, so the program entered the first if statement. 
#It then calculated the length of the word 'how' and returned it back as 3.




