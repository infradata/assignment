user_input = int(input('Enter a positive integer: '))
for i in range(1,user_input+1):
    if user_input % i == 0:
        print('{0} is a divisor of {1}'.format(i,user_input)) 
