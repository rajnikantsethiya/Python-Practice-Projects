def Main():
    yield 'you are awesome !'
    yield 'life in injoy !'

temp = Main()
print(temp) # holds reference
print(next (temp))
print(next (temp))

def sub():
    received = yield
    while True: # infinite generator
        print(received)
    
temp = sub()
next(temp)
temp.send("You") # send param to generators
temp.close() # teminating the generators


