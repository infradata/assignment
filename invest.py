def invest(amount, rate, time):
    for t in range(1,time+1):
        amount = amount + (amount * rate)
        print("year {0}: {1}".format(t,amount))

amount = float(input("Enter amount :"))
rate = float(input("Enter rate :"))
time = int(input("Enter years :"))

print("principal amount: ",amount)
print("annual rate in return : ",rate)
invest(amount,rate,time)

