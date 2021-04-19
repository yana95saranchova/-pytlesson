#task1

name="Yana"
day="19.04"

#1
print(f'Good day {name}!{day} is a perfect day to learn some python')

#2
s="Good day {0}! {1} is a perfect way to learn some python"
print(s.format(name, day))

#task2

name="Yana"
surname="Saranchova"
s=f"Good evening, {name} {surname}!"
print(s.format(name,surname))
name="Yana"
surname="Saranchova"
s=f"Good evening, {name} {surname}!"
print(s.format(name,surname))
#task3

a=58
b=17
print("a=58,b=17")
print('Addition=',a+b)
print('Substraction=',a-b)
print('Multiplication=',a*b)
print('Division=',a/b)
print('Exponent(power)=',a**b)
print('Modulus=',a//b)
print('Floor division',a%b)