# for x in range(1,11):
#     print(x*2)

# stnts = {"Aliyan":20 , "Mujtaba":19 , "Sufiyan":18}

# # print(stnts)

# # print(stnts["Mujtaba"],"\n")

# # for x in stnts:
# #     print(x,stnts[x])

print("\n\n\n\n Start Here : \n")


list1 = ["first","second","third",4,5,6,7,8,9,False]

print(list1)

x = int(input(""" What you want to do 
    1:Enter New value inside list
    2:Enter New Value in the end of list
    3:Delete value from list 

choice : """))

if x == 1:
    print(list1)
    value = int(input("Where you want to input the value : "))
    list1[value] = input("Enter : ")
elif x == 2:
    print(list1)
    list1.append( input("Enter : "))
elif x == 3:
    print(list1)
    value = int(input("Which Value you want to Delete : "))
    del(list1[value])
else :
    print("\n Wron Value fed")

print("\n\nNow list Becomes \n",list1,"\n\n\n\n")


stringg = 's'
print(type(stringg))

#   Prime numbers

# for lo in range(2,101):
#     prime = True
#     for nl in range(2,int(lo/2)):
#         if  lo%nl == 0:
#             prime = False
#             break
    
#     if prime:
#         print(f"{lo} is prime ")            
#             # print(f"lo:{lo} = nl:{nl} = %:{lo%nl}")
