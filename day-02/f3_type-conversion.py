# type conversion
# 1. implicit --- compiler
a = 23
print(a)
print(type(a))

name = "hari"
print(type(name))

height = 5.6
print(type(height))

# 2. explicit type conversion ---programmar
height =  int(height)
print(height)
print(type(height))

height = str(height)
print(type(height))
print("----------------------------------")
height = height +"5" 
print(height)  
print(type(height)) 
 