#lab 8-1
def num_sum(num):
    #creating a function for the sum of the numbers 
    sum = 0
    #creating a variable for the function 
    for x in range(num+1):
        sum += x
    return(sum)
    
#creating a for loop to check over every number from 0 up to the input, that merges them with the sum of the function 

x = input("Please input a number you would like to find the sum of all the numbers up to and including itself: ")
#making an input to display to the user the question
print(num_sum(int(x)))
#printing the answer according to the inputted number 