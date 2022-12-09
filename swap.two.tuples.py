#Write a python program to Swap two tuples in Python.
tuple1=("10","20")
tuple2=("40","50")
print("Tuple1 is {} & Tuple 2 is {}".format(tuple1,tuple2))
tuple1=tuple2[0],tuple2[1]
tuple2=tuple1[0],tuple1[1]
print("Tuple1 is {} & Tuple 2 is {}".format(tuple1,tuple2))
