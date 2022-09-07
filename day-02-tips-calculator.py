#this program gets the bill total, number of persons to share the bill and the percentage of tip they want to give
# retuns the amount to be paid by each including the tips
print('Welcome to the tips calculator')

bill_amount=float(input('Please enter the total bill amount \n'))

no_of_persons=int(input('Please enter how many people to split the bill\n'))

tips_percent=int(input('Please enter the percentage you want to give as tips 5% 10% 12% 15%\n'))

tips_amount=bill_amount*(tips_percent/100)

total_amount=bill_amount+tips_amount

bill_after_split=round(total_amount/no_of_persons,2)

print('The amount to be paid by each is $%.2f' % bill_after_split)