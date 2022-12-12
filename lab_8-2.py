# lab 8-2

def name_list(people):
    for z in people:
        print("Hi "+z+", you're invited to my party on Friday!")
#made function to print the name of each person, telling them they are invited to my party on friday
z = input("Would you like to input another name? Y/N: ")
new_people = z.lower() == "y"
#made input for wether or not the user would like to invite another person to their party

people = []
#an empty list for the names to be compiled in
while (new_people == True):
    people.append(input("Please input the name of the person you would like to invite to the party: "))
    z = input("Would you like to input another name? Y/N: ")
    new_people = z.lower() == "y"
#creating a loop that promts the user for the name of who they would like to invite, the name is added and the loop keeps asking for any more names until the user indicates they dont want any more people invited to the party 
name_list(people)
#made another list for the names combined