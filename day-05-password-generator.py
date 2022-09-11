#This program takes input from users like hw amny letters to be included in passwords,
# how many symbold should be included in the passwords, how many numbers needed to include and generates a password.
import random
letters=[chr(x) for x in range(65,91)]
upper_case=[chr(x) for x in range(97,123)]
letters.extend(upper_case)
print(letters)
numbers=[x for x in range(0,10)]
print(numbers)
symbols=['!','@','#','$','%','^','&','*','(',')']

print('Welcome to password generator!')
l=int(input('Enter the number of letters you needed to include:\n'))
n=int(input('Enter the number of numbers to include:\n'))
s=int(input('Enter the number of symbols to include:\n'))

password=''
for i in range(l):
    password+=random.choice(letters)
for i in range(n):
    password+=str(random.choice(numbers))
for i in range(s):
    password+=random.choice(symbols)

ps=list(password)
random.shuffle(ps)
password=''.join(ps)
print(f'The password is {password}')