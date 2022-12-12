def count_a(word):
    #creating a function to count how many letter "a"'s are in a string
    lowered_word = word.lower()
    lowered_word[::-1]
    count = 0
    num_a = 0
    while (count < len(lowered_word)):
        if (lowered_word[count] == "a"):
            num_a += 1
        count += 1
    return (num_a)
    #defining a count for the while loop and the number of a's that are detected
x = input("Input any word to find out how many a's it contains : ")
#prompting the user to input a word to find out how many a's are in it 
print(count_a(x))
#prints the answer to how many a's are in the word 