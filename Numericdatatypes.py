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
name_2 = 'videm shireesha'
# print(name_2[6])

#finding sub sting in a main string is called slicing
#sub = 'i'
#print(name_2.find("s"))
#rfind
#print(name_2.rfind(sub))

#index("x")
#print(name_2.index("s"))
#print(name_2.rindex("i"))
#count("x")
print(name_2.count("s"))

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
#marks = ['20','45','67','55','89']
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


# family[1:2]= ["aishu","pavan"] #slicing multiple items in the list in a particular index
# print(family)
# family.remove("aishu") #it will remove the item in the list
# print(family)
# print(family.pop(0)) #it will display the item given in the index

#a.upper() it will convert the given string to uppercase
# string = "marolix technology solutions"
# print(string.upper())
#b.lower() it will display the given string to lowercase
#print(string.lower())
#c.swapcase() when i/p is in lowercase then it will convert into uppercase and vice versa
#string_1 = "marolix technOLOGY SOLUTIONS"
#print(string_1.swapcase())
#d.title() it will convert only the first letter of the word
#print(string.title())
#capital()
# str = "hello my friend"
# print(str.capitalize())

# startswith() it will defaultly check whether the input is starts (given) or not
# url = "www.ibomma.com"
# print(url.startswith("http"))
# endswith() same as startswith but it will check end value
# email = "videmshireesha@gmail.com"
# print(email.endswith("@gmail.com"))

#3.Tuple()
#friends = ("ramya","roshini","sanvitha",[1,2,3,4])
# print(type(friends))
#print(friends[::-1])
# friends[3][0] = "nikhil"
# print(friends)

#4.boolean it has only true(1) false(0) values
# siri = True
# bablu = False
# print(type(siri))
# print(type(bablu))

# a = 99
# b = 0
# print(a==b)
# print(bool(a)) # other than 0 all values are true
# print(bool(b))

#5.set is a unordered list
colors = {'red','green','white','blue','black'}
print(type(colors))
print(colors)
# add is used to add only 1 item
colors.add("orange")
print(colors)
# update is used to add a list of items(multiple)
colors.update(['yellow','brown','sea green'])
print(colors)