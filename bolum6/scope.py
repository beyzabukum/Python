x="global x"
def function():
    x="local x"
    print(x)

function()
print(x)

#############################

name="çınar"
def changeName(new_name):
    name=new_name
    print(name)
changeName("ada")
print(name)


#######################

name="global string"
def greeting():
    name="çınar"
    def hello():
        print("hello"+ name)
    hello()
greeting()            

########################

x=50
def test(x):
    print(f"x: {x}")
    x=100
    print(f"changed x to {x}")
test(x)
print(x)