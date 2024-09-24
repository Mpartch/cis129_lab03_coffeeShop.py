#Mia Partch
#CIS 129
#lab03_coffeeShop

muffin=int(input("How many muffins will you be purchasing?"))
coffee=int(input("How many cofffee cups will you be purchasing?"))
cakePop=int(input("How many muffins will you be purchasing?"))
scone=int(input("How many cofffee cups will you be purchasing?"))

coffeePrice=(coffee*5)
muffinPrice=(muffin*4)
cakePopPrice=(cakePop*4)
sconePrice=(scone*4)



tax=((coffeePrice+muffinPrice+sconePrice+cakePopPrice)*0.06)
totalPriceWTax=((coffeePrice+muffinPrice+sconePrice+cakePopPrice)+tax)

print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffee)
print("Number of coffees bought?")
print(muffin)
print("Number of cake pops bought?")
print(cakePop)
print("Number of scones bought?")
print(scone)
print("***************************************")
print("                                       ")
print("***************************************")
print("My Coffee and Muffin Shop Reciept")
print(coffee, "Coffee at $5 each: $",coffeePrice)
print(muffin, "Muffins at $4 each: $",muffinPrice)
print(cakePop, "Cake pops at $4 each: $",cakePopPrice)
print(scone, "Scones at $4 each: $",sconePrice)
print("6% tax: $",tax)
print("---------")
print("Total: $", totalPriceWTax)
print("---------")
print("Thank you for shopping at Cakes&Coffees! Customers like you make our dreams possible")
