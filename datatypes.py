#Data types program
print('Data types')

#Numeric (int, float, complex)
# marks = 525
# percentage = (marks/600)*100
# print('percentage',percentage)

# print(type(marks))
# print(type(percentage))

#complex data type
# x = 3 + 5j
# print(type(x))
# print(x.real)
# print(x.imag)
# print(x.conjugate()) 

#sequence operators
# 1.strings
# name = ''' Shireesha
# knows
# about
# python '''
# print(name)
# name_1 = name.rstrip() #strip which removes spaces from both left and right on tha string
# print(name_1)
# print(len(name_1))

#indexing
#name_2 = 'videm shireesha'
# print(name_2[6])

#finding sub sting in a main string is called slicing
#sub = 'i'
# print(name_2.find(sub))
#rfind
#print(name_2.rfind(sub))

#index("x")
# print(name_2.index("r"))
#print(name_2.index("i"))

#slicing
# print(name_2[1:8])
# print(name_2[0:28:2])
# print(name_2[::-1])

#replacing
#v = "shireesha is bad girl"
# sub_string = "good"
# v1 = v.replace("bad",sub_string)
# print(v1)

#splitting
# s = "learning@python@is@not@easy"
# x = s.split("@")
# print(x)

#List concept

# numbers = input("enter numbers: ")
# lst = numbers.split(",")
# print(numbers)
# print(type(lst))
# print(lst)

#joining two strings
family = ["nishanth","shireesha","santhosha","sudharshan"]
#dt = ["14","09","2023"]
# s = "-".join(family)
# print(s)
# print(len(family))

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


family[1:2]= ["aishu","pavan"] #slicing multiple items in the list in a particular index
print(family)
family.remove("aishu")
print(family)
print(family.pop(0))