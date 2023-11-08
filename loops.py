x= 0
y = 5
stringin = "Peter"
list1=[1,2,2,2,3,4,5]
#For Loops

#no definition of count neede
#change the above count to value1 to demo the next point
for count in range(0,y,1):
    print("for",count)
#########################
# be carefule with these loops    
for count in list1:
    print("for in list", count,list1[count])
for index, element in enumerate(list1):
    print("Element at index", index, ":", element)
##############################
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
        