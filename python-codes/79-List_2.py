'''
Typing many numbers and including in a list, if this number already exist
it won't be add, at the end, all add numbers will be shown (crescent order)
'''
#Creating an empty list;
my_list = []
#Using infinite looping to get how many numbers you want;
while True:
    my_list.append(int(input("Type numbers as you want and -0 to check the list: " )))
    #Setting the stop condition;
    if -0 in my_list:
        #Removing the -0 condition;
        my_list.pop()        
        #Getting the right list excluding the duplicates and putting in crescent order;
        final_list = sorted(set(my_list))
        print(f"Here is the final list : {final_list}")
        break
