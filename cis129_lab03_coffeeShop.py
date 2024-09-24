#Mia Partch
#CIS 129
#lab03_coffeeShop

muffin=int(input("How many muffins will you be purchasing?"))
coffee=int(input("How many cofffee cups will you be purchasing?"))
coffeePrice=(coffee*5)
muffinPrice=(muffin*4)
tax=((coffeePrice+muffinPrice)*0.06)
totalPriceWTax=((coffeePrice+muffinPrice)+tax)

print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffee)
print("Number of coffees bought?")
print(muffin)
print("***************************************")
print("                                       ")
print("***************************************")
print("My Coffee and Muffin Shop Reciept")
print(coffee, "Coffee at $5 each: $",coffeePrice)
print(muffin, "Muffins at $4 each: $",muffinPrice)
print("6% tax: $",tax)
print("---------")
print("Total: $", totalPriceWTax)


