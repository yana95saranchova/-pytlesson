#task1

#part1
s="hello world"
if len(s)<2:
    print()
else:
    result=s[:2]+s[-2:]
    print(result)

#part2
s='my'
if len(s)<2:
    print()
else:
    result=s[:2]+s[-2:]
    print(result)

#part3
s="x"
if len(s)<2:
    print()
else:
    result=s[:2]+s[-2:]
    print(result)


#task2
i='0939453682'
if len(i) == 10 and i.isdigit():
    print('It is a valid telephone number, which contains only numbers and is only 10 numbers long')
elif len(i)!=10 and i.isdigit():
    print('It is a invalid telephone number, which contains only numbers but has not only 10 numbers')

#task3
name='yana'
print('Input your login')
login='Yana'
if name.lower()==login.lower():
    print("it is correct way to input")

#задание 3 вообще не пошло(