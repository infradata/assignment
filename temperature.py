def c2f(celsius):
    return float(celsius) * 9/5 + 32

def f2c(fahrenheit):
    return (float(fahrenheit) - 32) * 5/9


fahrenheit = input("Enter fahreinheit values : ")
celsius = input("Enter celsius values : ")


print("{0} degrees F = {1} degrees C".format(fahrenheit,f2c(fahrenheit)))
print("{0} degrees C = {1} degrees F".format(celsius,c2f(celsius)))

