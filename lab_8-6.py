#lab 8-6
num = int(input("Input a number ")) 
#input statement asking the user to enter a number

def factorial(num): 
#making function for the number inputted
    x = 1
    z = 1
    while num >= x: #making the loop to find the factorial
        z = z * x
        x += 1
    return z #return the factorial after the loop 

print(factorial(num))