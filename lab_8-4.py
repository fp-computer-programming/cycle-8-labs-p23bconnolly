def sum(n): #making function to find total 
    i=0
    total = 0
    while i<(n+1): #making while loop
        total += i
        i+=1
        
    return total #returns the total of the sum
print(sum(5))