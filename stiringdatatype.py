# 1.strings
# name = ''' Shireesha
# knows
# about
# python '''
# print(name)
# name_1 = name.rstrip() #strip which removes spaces from right on the string
# name_1 = name.lstrip() #strip which removes spaces from left on the string
# print(name_1)
# print(len(name_1))

#indexing
name_2 = 'videm shireesha'
# print(name_2[6])

#finding sub string in a main string is called slicing
# sub = 'i'
# print(name_2.find("s"))
# # rfind
# print(name_2.rfind("i"))

#index("x")
print(name_2.index("s"))
print(name_2.rindex("i"))
# count("x")
print(name_2.count("s"))

#slicing
# print(name_2[1:8])
# print(name_2[0:28:2])
# print(name_2[::-1])

#replacing
# v = "shireesha is bad girl"
# sub_string = "good"
# v1 = v.replace("bad",sub_string)
# print(v1)
# print(v.replace("bad","good"))

#splitting
# s = "learning@python@is@not@easy"
# x = s.split("@")
# print(x)


#a.upper() it will convert the given string to uppercase
string = "marolix technology solutions"
# print(string.upper())
#b.lower() it will display the given string to lowercase
#print(string.lower())
#c.swapcase() when i/p is in lowercase then it will convert into uppercase and vice versa
#string_1 = "marolix technOLOGY SOLUTIONS"
#print(string_1.swapcase())
#d.title() it will convert only the first letter of the word
# print(string.title())
print(string.insert(1,"siri"))
#capitalize()
str = "hello my friend"
print(str.capitalize())

# startswith() it will defaultly check whether the input is starts (given) or not
url = "www.ibomma.com"
print(url.startswith("http"))
# endswith() same as startswith but it will check end value
email = "videmshireesha@gmail.com"
print(email.endswith("@gmail.com"))

print(string.center(4))
print(string.casefold())
print(string.encode())
print(string.expandtabs())
print(string.format())
print(string.ljust(3))
print(string.rpartition("i"))
