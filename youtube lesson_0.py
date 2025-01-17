libary =[]
wish_list = []

user_Q1 = input("Enter the books your own separated by comma: ").capitalize().split(", ")
libary.extend(user_Q1)
print (f"your libary: {' , '.join(libary)}.")

user_Q2 = input("\nEnter a books you wish to have separated by comma: ").capitalize().split(", ")
wish_list.extend(user_Q2)
print (f"your wish_list: {' , '.join(wish_list)}.")

user_Q3 = input("\nEnter the name of a book from your wish_list that you've acquired \
or prss enter to skip: ")
if user_Q3 in wish_list:
    wish_list.remove(user_Q3)
    libary.append(user_Q3)
else:
    print(f"you may don't have one of this books: {user_Q3} ")    

print (f"\nUpdate libary: {' , '.join(libary)}")
print (f"Update wish_list: {' , '.join(wish_list)}")

user_Q4 = input("\nEnter the name of a book from your libary that you wish to donate \
or press enter to skip: ").capitalize().split(", ")
if user_Q4 in libary:
    libary.remove(user_Q4)
else:
    print(f"you may don't have one of this books: {' , '.join(user_Q4)} ")      

print (f"\nFinal libary after donation: {' , '.join(libary)}")

