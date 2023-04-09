try:
    num = int(input("Enter an interger  "))
    print(num)
except ValueError:
    print('you had to put an integer :o')
except ZeroDivisionError:
    pass
finally:
    print("ye to hoga runn")

age = int(input(" age :"))

if age<18:
    raise ValueError("Aap abhi chote ho ")