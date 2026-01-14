# Strings 
x = "This is practice test"
y = 'Program 1'
z = x + ' ' + y
print(f"Value for z is: {z}")

x = "Virat kohli"
print(x.replace("V", "C"))
x = "     test    "
print(x.strip())
x = "HELLO"
print(x.casefold())
x = "hello"
print(x.capitalize())

# Numbers
a = 1 # int
b = 2.1 #float
print(a+b)
print(int(a+b))

# Tuples
a = ("hello", "test", "practice")
print(a[1])
b = ("This", "is", "good")
print(a + b)
# access tuples
print(a[0], a[2])
print(a[0:2])

# update tuples
temp = list(a)
temp.append("session")
a = tuple(temp)
print(a)

# unpack tuples
a = ("name", "age", "weight")
x,y,z = a
print(x,y,z)

x, *y = a
print(x,y)

a = ("name", "age", "weight", "height", 2,4,5)
x, *y, z = a
print(x,y,z)

del a
print(a)


# loop
a = ("name", "age", "weight")
if "age" in a:
    print("Yes its present")
else:
    print("its not present")

print(range(len(a)))
for i in range(len(a)):
    print(i)


# Frozen sets
# This is similar to an Object.freeze() in js
c = frozenset({"indore", "mumbai", "pune"})
print(c)
print(c.union(a))


