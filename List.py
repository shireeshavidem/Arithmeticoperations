#List[] concept

# numbers = input("enter numbers: ")
# lst = numbers.split(",")
# print(numbers)
# print(type(lst))
# print(lst)

#joining two strings
#family = ["nishanth","shireesha","santhosha","sudharshan"]
#dt = ["14","09","2023"]
# s = "-".join(family)
# print(s)
# print(len(family))
#print("-".join(family))

#lst = [] #empty list
#print(type(lst))

# nested list or multi dimensional list

# biodata = ["22",'20/11/2001','address',family]
# biodata[1] = '2/11/2001'
# print(biodata)


# Accessing element from list
# print('brother',family[0])
# print('father',family[-1])
# print(biodata[3][-1])
# print(biodata[::-1]) #slicing
# print(biodata[1:3])
 

#replacing marks in list
marks = ['20','45','67','55','89']
# marks[0] = '58'
# print(marks)
# print(marks.update('20','58'))

# surname = "videm"
# name = "shireesha"
# print(surname + name) #concatention
# rep = name*5 #repeating
# print(rep)

# print(marks + family)
# print(marks*2)
# family.append("vignesh") #append will add given single item to the list
# family.append(["aishu","pavan"]) #append will add given multiple item to the list
# print(family)
# family.insert(1,"aishu")
# print(family)


# family[1:2]= ["aishu","pavan"] #slicing multiple items in the list in a particular index
# print(family)
# family.remove("aishu") #it will remove the item in the list
# print(family)
# print(family.pop(0)) #it will display the item given in the index

list = []
n = int(input("enter no of elements: "))
for i in range(0,n):
    lst1 = input("enter your elements: ")
    list.append(lst1)
print(list)   