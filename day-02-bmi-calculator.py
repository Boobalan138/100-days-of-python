#This bmi calculator program takes weight and height from the user and return the bmi as whole number

height=input('Enter your height in meter\n')
weight=input('Enter your weight in kg\n')

bmi=int(float(weight)/float(height)**2)
print('Your BMI is '+str(bmi))
