rows = [["Darick", "Eugene", "Kyle", "Azaan"], ["Ryan",
"Phil", "Eman", "Alex", "Nicholas"],
["Christian", "Josh", "Matt", "Francesco"],
["Patrick", "Nico", "Trevayne"]]

for row in rows:
#making the loop
    for names in row:
#making loop so it prints each individual name
        if names[-1] == "s":
#if the names end in s add an' to make it possesive
            names+="'"
        else:
            names+="'s"
        print(names)
#printing the the names with an 's if needed 