# Examine SEC Guide and look at for loops
#1. For loops
for counter in range(10):    #counter is a variable that is assigned values from ? to ? (predict)
  print("Hello World", counter) # Counter has range 0 thru 9

print("Goodbye")

for i in range(1,10):  # range defined in loop statement 1 t0 9 is printed
    print("hello World2 ",i)# note that 10 is not printed
print("Goodbye again")

################ More for loops
x= 0
y = 5
stringin = "Peter"

#no definition of count needed
#change the above count to value1 to demo the next point
#look at ref Guide to evaluate the values in LOOP GUARD
#for count in range(0,y,1): #last value 1 is the step change to 2
for count in range(0,y,2): #last value 1 is the step change to 2
    print("for",count)

#########################
# be careful with these loops
list1=[1,2,2,2,3,4,5]
for element in list1: # in this case element takes on the value of list item when printed!!
    print("for in list", element,list1[count]) #element becomes the list item!!
    
for index, element in enumerate(list1):
    print("Element at index", index, ":", element)
##############################
"""
for index in range(len(list1)-1): #note loop guard does not use all arguments
  print ("list1[",index,"]",list1[index], "Index", index)
  
  
# the use of count in while is different, note it has not been defined for the FOR loop
# in advance
count = 0
while count < y:
    print("while",count)
    count += 1
    
forward = True
stop = 0
while forward:
    print("still running", stop)
    stop +=1
    if stop >=10:
        forward = False
"""        
