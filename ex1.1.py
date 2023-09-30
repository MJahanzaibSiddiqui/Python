#LIST

def print_list(st):
    print("List:", st)
list1 = ['ALI & ML', 'DBMS','SE', 2004, 'CX',8222]
# Calling the function to print list1
print_list(list1)

# UPDATE LIST!!

def update_list_element():
  list2 = ['a','b','c']
  print("before update", list2)
  list2[1]='z'
  print("after update", list2)
 #calling function
update_list_element()

# DELETE LIST
def delete_list_element():
  list2 = ['a','b','c']
  print("before delete", list2)
  del list2[1]
  print("after delete", list2)
 #calling function
delete_list_element()

def tuple_example():
    tuple1=('efgh',804,3.17)
    print(tuple1 * 2)
tuple_example()

def dictionary_example():
    student = {'name': 'John', 'age': 25, 'grade': 'A'}
    print(student)
dictionary_example()    

def if_else_example():
    value=10
    if value<10:
        deduction=value*0.03
        print ("Deduction",deduction)
    else:
        deduction= value*0.05
        print ("Total Value: ", value) 
        print("Deduction from value:", deduction)
    print("Remaining is: ", value-deduction)   
    
if_else_example()

def while_loop_example():
   count = 0
   while ( count < 3) :
     print("The count is:", count )
     count = count + 0.5
   print (" Day 1 with python!")
while_loop_example()

def for_loop_example():
 vegatables=['carrot','potato']
 for x in vegatables:
    print ('season vegatble:',x )
print("More Vegatables!")
for_loop_example()
    
























    
    

