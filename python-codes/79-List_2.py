'''
Typing many numbers and including in a list, if this number already exist
it won't be add, at the end, all add numbers will be shown (crescent order)
'''
#Creating an empty list;
my_list = []
#Inserting the first element in the list
my_list.append(int(input("Type numbers for the list: " )))
#Starting an infinite looping with while
while True:
    #the flag condition question to the user choose an option
    opt = str(input('Do you want to keep inserting numbers? [Y/N]: '))

    if 'y' in opt.lower():
        my_list.append(int(input("Type numbers for the list: " )))
    elif 'n' in opt.lower():                     
        #Getting the right list excluding the duplicates and putting in crescent order;
        final_list = sorted(set(my_list))
        print(f"Here is the final list : {final_list}")
        break
    #If the user try to insert a different option, it will result in a error msg.
    else:
        print("Sorry, type 'Y' for (yes) and 'N' for (no).")
    