#this program takes input from user 0 for rock, 1 for paper, 2 for scissor and checks with computer
#rock beats scissor, scissor beats paper, paper beats rock
import random

print('Welcome to the rock-paper-scissor game')

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor= '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def display(n):
    if n==0:
        print(rock+'\nRock')
    elif n==1:
        print(paper+'\nPaper')
    elif n==2:
        print(scissor+'\nScissor')
user_input=int(input('Enter 0 for Rock, 1 for paper, 2 for scissor\n'))
display(user_input)

computer_input=random.randint(0,2)
display(computer_input)
if user_input==computer_input:
    print('Match draw!')
else:
    if user_input==0:
        if computer_input==1:
            print('Computer Won!')
        elif computer_input==2:
            print('You Won! Congrats!')
    elif user_input==1:
        if computer_input==0:
            print('You Won! Congrats')
        elif computer_input==2:
            print('Computer won!')
    elif user_input==2:
        if computer_input==0:
            print('Computer Won!')
        elif computer_input==1:
            print('You won! Congrats')
