Height = float(input('Enter your height in centimeters: '))
Weight = float(input('Enter your weight in kilograms: '))
Height = Height/100
BMI = Weight/(Height*Height)
print('your Body Mass Index (BMI) is: ',BMI)
if (BMI > 0): 
    if (BMI<=16):
        print('You are severely underweight, please consider gain more weight')
    elif (BMI<=18.5): 
        print('You are underweight)')
    elif (BMI<=25):
        print('You are healthy, please keep up the good work!')
    elif (BMI<=30):
        print('You are overweight !')
    else: print('You are severely overweight, please consider excercising and healthy diet')
else: ('Please enter valid details')
        