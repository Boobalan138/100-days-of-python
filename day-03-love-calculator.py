#this program takes two names as inputs and searches for the occurence of the letters in true and love
# and returns the love score by concating them

print('Welcome to the love calculator')

name1=input('Enter the first name:\n')
name2=input('Enter the second name:\n')

name=name1+name2
name=name.lower()
true_occurence=name.count('t')+name.count('r')+name.count('u')+name.count('e')
love_occurence=name.count('l')+name.count('o')+name.count('v')+name.count('e')

score=str(true_occurence)+str(love_occurence)
score=int(score)

if score<10 or score>90:
    print(f'Your score is {score}, you will go together like coke and mentos.')
elif score>40 and score<50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}')
