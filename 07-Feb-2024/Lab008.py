# String Concatination

s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3) # good option to display concat
print(s1 + s2)

name = "kavita"
age = 42
# r = name + age TypeError: can only concatenate str (not "int") to str
# print(r)
r = name + str(age)
print(r)

g = 'Hello'
#g += 'world' # other option used gives same result
#print(g)
g = g + 'world'
print(g)

## Increment & Decrement ++ & --

x = 5
x -= 0
x += 3
print(x)

x = 10
# y = x+1