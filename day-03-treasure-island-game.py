#This game is based based on the user's input
#there is two ways before the user, left and right one leads to river and another to hole
#On river side, you can either swim or wait for boat to arrive
#there will be three doors, one door will unlock treasures to you, while others having many dangers to bring to you

print('Welcome to treasure island!')
print('Find the treasures and become a super hero')
print('if not, you will be finished in the island itself.!')

print('There is two passages infront of you!')
step1=input('Choose one passage left or right:\n')
if step1.lower()!='left':
    print('You fall into the hole.\nGame Over.')
elif step1.lower()=='left':
    print('You arrived the river\nWhat you want to do?\n')
    step2=input('Want to wait or swim to cross the river?\n')
    if step2.lower()!='wait':
        print('Attacked by trout.\nGame Over')
    elif step2.lower()=='wait':
        print('A boat has arrived the river side.\nTake the boat and cross the river')
        print('There is a passage passing through the jungles on the other side of the river.')
        print('The passage goes deeper into the woods and suddenly goes into under ground')
        print('There are three doors infront of you\nRed, Blue and Yellow')
        step3=input('Choose one door to open!\nRemember you can only one chance:\n')
        if step3.lower()=='red':
            print('You are burned by fire.\nGame Over!')
        elif step3.lower()=='blue':
            print('You are eaten by beasts.\nGame Over!')
        elif step3.lower()=='yellow':
            print('You unlocked the treasure!!!\nYou win!!!')
        else:
            print('Game Over.')