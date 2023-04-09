# try:
#     f = open('files_learnin.txt','x')
# except FileExistsError:
#     print("file already there....")

name = input("Enter your name stranger.. ")

f = open('files_learnin.txt','a+')
f.write(f"\nhellooo {name} \nyour should be death 40s from now.....")

nf = open('C:/Users/Shery/Downloads/1.txt','r')
print(nf.readline())

def authenticate(func):
        user = input("Enter your username:")
        password = input("Enter your password:")
        if (user,password) == ('admin','password'):
            return func()
        else:
            print("Invalid username or password")

@authenticate
def my_function():
    print("Access granted.")

my_function()