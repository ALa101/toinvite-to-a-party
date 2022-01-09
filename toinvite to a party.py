"""
   Ask the user to enter the names of three people
   they want toinvite to a party and store them in a list.
   After they have enteredall three names,
   ask them if they want to add another.
   If they do,allow them to add more names until they answer “no”.
   Whenthey answer “no”,
   display how many people they have invited tothe party.
   and upload file to GitHub and past the link down
"""


people=[]
print("Enter the names of three people they want toinvite to a party :\r")
for i in range(3):
    people.append(input())
print("People invited to the party")
for pe in range(len(people)):
    print(str(pe + 1) + "." + people[pe], end='\t')
add = input("\nDo you want add another ?\n\t\ty or n\n")
while add != 'n' and add != 'y':
    print("Pleace chose yes ( y ) or no ( n )")
    add = input("\nDo you want add another ?\n\t\ty or n\n")
else:
    while add == 'y':
        people.append(input("Enter the names : "))
        add = input("Do you want add another ?\n\ty or no")
    else:
        print("the count of people that toinvite to party: " + str(len(people)))
        for pe in range(len(people)):
            print(str(pe + 1) + "." + people[pe], end='\t')












