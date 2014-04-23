print ("""What do you want to buy?
1. Soda 20
2. Rice ball 35
3. Pizza 300
4. Beef steak 350""")
good = int(input("I want to buy.. "))
print ("How much money do you give me?")
money = int(input(""))
if good ==1:
	good = 20
elif good ==2:
	good = 35
elif good ==3:
	good = 300
elif good ==4:
	good = 350
remain = money - good
print("I return to you %s."%(remain))
changeList = [1000,500,100,50,1]
for change in changeList:
	print("{} {} change(s)".format(remain//change,change))
	remain = remain%change
print("Thanks for you patronage, bye bye!")
input("press Enter to exit...")