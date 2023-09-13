#Data types program
print('Data types')

#Numeric (int, float, complex)
marks = 525
percentage = (marks/600)*100
print('percentage',percentage)

print(type(marks))
print(type(percentage))

#complex data type
x = 3 + 5j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate()) 

#strings
name = ''' Shireesha
knows
about
python '''
print(name)
name_1 = name.rstrip() #strip which removes spaces from both left and right on tha string
print(name_1)
print(len(name_1))

#indexing
name_2 = 'videm shireesha'
print(name_2[6])

#finding sub sting in a main string
sub = 'i'
print(name_2.find(sub))
print(name_2.rfind(sub))
