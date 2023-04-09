# from numpy import inner


# def outer():
#     print("this is outer func")
    
#     def inner():
#         print("this is inner func")
    
#     inner()
    

# outer()


# def fact(x):
#     if  x == 1:
#         return 1
#     else:
#         return x*fact(x-1)
    

# print(fact())



def arguments(**args):
    print(args)

arguments(d='11',s='33', a='d')

x = lambda a: a**2

print(x(5))

zlist = ['a','s','e','h','q','c','u','p','r','t']
print(sorted(zlist , reverse=True))

mylist=[1,2,3,4,5,7,1,2,3,4,6,8,0,6,5]

mylist = list(set(mylist))

print(mylist)


def tointeger(ans):
    try:
        int(ans)
        return True
    except ValueError:
        return False

print(tointeger("123"))
print(tointeger("a5sn"))
print(tointeger("A"))
print(tointeger(""))