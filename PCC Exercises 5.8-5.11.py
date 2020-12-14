#5.8
#Make a list of five or more usernnames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. 
#Loop through the list, and print a greeting to each user:
#If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report? 
#Otherwise, print a generic greeting, such as Hello Eric, thank you for loggin in again.  

active_users = ['salad.fingers', 'phil.defranco', 'john.lennon', 'admin', 'mao.zedong', 'zen.daya'] 
if active_users: 
    for user in active_users: 
        if user != 'admin':
            print(f"Welcome back master/mistress {user.title()}")
        else: 
            print("""Oh, it's you, welcome back, scum of the earth, I wouldn't touch you with a 39 and a half foot pole lookin' ass,'I drop off a KFC famous bowl every other weekend what do you mean I don't pay child support lookin ass', better get yo fuckin' slim jim fingers off my keyboard and get gone""".title())
else: 
    print('We need to find some users!'.title())

#5.9: Add an if test to hello_admin.py to make sure the list of users is not empty.
#If the list is emtpy, print the message We need to find some users!
#Remove all of the usernames from your list, and make sure the correct message is printed. 

######The code written in 5.8 actually fufills these conditions, I was having too much fun

#5.10: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
#Make a list of five or more usernames called current_users. Make another list of five usernames called new_users. 
#Make sure one or two of the new usernames are also in the current_users list.
#Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. 
#If a username has not been used, print a message saying that the username is available.
#Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 

current_users = ['Ginny Weasley', 'Luna Lovegood', 'Neville Longbotom', 'Hermoine Granger', 'Sirius Black(RIP)', 'Harrymus Pottermus']

new_users = ['Rubeus Hagrid', 'Severus Snape', 'Hermoine Granger', 'Draco Malfoy', 'Albus Dumbledore', 'Dolores Umbridge', 'Luna Lovegood', 'Ron Wealey'] 

for user in new_users: 
    if user.title() in current_users: 
        print('Sorry that username is already in use, PICK ANOTHER ONE') 
    elif user.lower() == 'draco malfoy': 
        print('Get the fuck out of here death eater!') 
    else: 
        print ('That username is available! Do you want to use it though?')



#5.11: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
#Store the numbers 1 through 9 in a list.
#Loop through the list.
#Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. 
#Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line. 

ordinal_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 

for num in ordinal_nums: 
    if num == '1': 
        print ('1st')
    elif num == '2': 
        print ('2nd') 
    elif num == '3': 
        print('3rd') 
    else: 
        print((num) + 'th')





