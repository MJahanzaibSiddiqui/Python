def unique_list():
    list = [1,1,2,3,3]
    print("Original list:",list)
    if (list[0]!=list[1]):
        print("unique value at 1st position")
        print("Value is:",list[1])
    elif (list[1]!=list[2]):    
       print("unique value at 2nd position")
       print("Value is:",list[2])
    elif (list[2]!=list[3]):   
        print("unique value at 3rd position") 
        print("Value is:",list[3]) 
    elif (list[3]!=list[4]): 
        print("unique value at 4rth poistion")
        print("Value is:",list[4]) 
    else:
        print("All same. ")    
unique_list()

#UPPer wala bhi sahi hai lekin acha nhi hai

# def unique_list():
#     list1 = [1, 1, 2, 3, 3]
#     print("Original list:", list1)
#     # Check for unique values and print their positions
#     for i in range(len(list1) - 1):
#         if list1[i] != list1[i + 1]:
#             print("Unique value at position:", i + 1)
        

# unique_list()


#ye bhi manual ke according nhi hai. 