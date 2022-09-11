#This program prints fizz if the number divisible by 3 and buzz if the number divisible by 5 fizzbuzz if the number divisible by both 3 and 5

n=int(input('Enter the number you need to print upto:\n'))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    else:
        print(i)