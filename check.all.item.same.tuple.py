#Write a python program to check if all items in the tuple are the same.
tuple1=("java","java","java","java","java")
flag=True
for e in tuple1:
    if e=="java":
        flag=True
    else:
        flag=False
if flag==True:
    print("All elements are the same")
else:
    print("Sorry,All element are not same") 