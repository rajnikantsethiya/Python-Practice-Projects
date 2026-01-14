#List , This is just like Array in js, methods would be different
# List can be collections of items of different data types
print("List starts from here:::::::::::")
x = [1,2,3,5,6,7, "Hello"]
print(x)
print(x[3])
print(x[1:4])
print(x[4:])
x.append(8)
print(x)
x.remove("Hello")
print(x)
y = [11,23,12,4,43,23]
x.extend(y)
print(x)
print(x.pop())
x.reverse()
print(x)
x.sort()
print(x)
x = [1,2,3,4,5,5,5,6,7,7]
listComprehention = [i for i in x if i > 3 in x]
print(f"List comprehention example:{listComprehention}")
#Set
# Set is a collection of unique elements, 
# which order is not fixed. If we have 2 sets, we can check the union(all elements), intersection(common elements)
print("Set starts from here:::::::::::")
a = set({"tea", "whisky", "rum"})
b = set({ "coffee", "tea", "mojito"})
print(a, b)
print(f"Unique items:{a | b}")
print(f"Common items:{a & b}")
a.add("wine")
print(a)
print(a.intersection(b)) # can use methods as well as symbols like | and &

#Dict
# This is more like Object in other programming lang like js
print("Doctionary starts from here:::::::::::")
q = dict({
    "name": "raj",
    "age": 33
})
q.update({"color": "fair"})
print(q)
print(q.fromkeys(q))
print(q.keys())
print(q.get("name"))
print(q.pop("name"))
print(q.popitem())
print(q, q.values())


#Byte arrays
# TODO