# $550, 1200 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
class covfefe:
    """A class that contains parameters of coffee types"""
    def __init__(self, money, water, milk, coffee, dcups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.dcups = dcups


class twogirls1cup:
    """A coffee machine class"""

    # available coffee types
    espresso = covfefe(4, 250, 0, 16, 1)
    latte = covfefe(7, 350, 75, 20, 1)
    cappuccino = covfefe(6, 200, 100, 12, 1)

    def __init__(self, money, water, milk, coffee, dcups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.dcups = dcups
        self.state = "select action"
        print("Write action (buy, fill, take, remaining, exit):")

    def setmainmenu(self):
        self.state = "select action"
        print("Write action (buy, fill, take, remaining, exit):")

    def check(self, coffee_type):
        if self.water - coffee_type.water < 0:
            print("Sorry, not enough water!")
            return False
        if self.coffee - coffee_type.coffee < 0:
            print("Sorry, not enough coffee beans!")
            return False
        if self.dcups - coffee_type.dcups < 0:
            print("Sorry, not enough disposable cups!")
            return False
        return True

    def make(self, coffee_type):
        enough = self.check(coffee_type)
        if not enough:
            return
        print("I have enough resources, making you a coffee!")
        self.money += coffee_type.money
        self.water -= coffee_type.water
        self.milk -= coffee_type.milk
        self.coffee -= coffee_type.coffee
        self.dcups -= coffee_type.dcups

    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def __str__(self):
        a = "The coffee machine has:\n"
        a += str(self.water) + " of water\n"
        a += str(self.milk) + " of milk\n"
        a += str(self.coffee) + " of coffee beans\n"
        a += str(self.dcups) + " of disposable cups\n"
        a += "$" + str(self.money) + " of money"
        # a += str(self.money) + " of money"
        return a

    def buy(self, drink):
        if drink == "back":
            pass
            # self.setmainmenu()
        elif drink == "1":
            self.make(self.espresso)
        elif drink == "2":
            self.make(self.latte)
        elif drink == "3":
            self.make(self.cappuccino)
        else:
            print("oxyel?")

    def evaluate(self, userinput):
        if self.state == "select action":
            action = userinput
            if action == "exit":
                exit()
            if action == "buy":
                self.state = "select coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
            elif action == "fill":
                # self.fill()
                self.state = "filling 1"
                print("Write how many ml of water do you want to add:")
            elif action == "take":
                self.take()
                self.setmainmenu()
            elif action == "remaining":
                print(self)
                self.setmainmenu()
            else:
                print("Unknown action, uno-dos-quattro")
        elif self.state == "select coffee":
            drink = userinput
            self.buy(drink)
            self.setmainmenu()
        elif self.state == "filling 1":
            add_water = int(userinput)
            self.water += add_water
            self.state = "filling 2"
            print("Write how many ml of milk do you want to add:")
        elif self.state == "filling 2":
            add_milk = int(userinput)
            self.milk += add_milk
            self.state = "filling 3"
            print("Write how many grams of coffee beans do you want to add:")
        elif self.state == "filling 3":
            add_coffee = int(userinput)
            self.coffee += add_coffee
            self.state = "filling 4"
            print("Write how many disposable cups of coffee do you want to add:")
        elif self.state == "filling 4":
            add_cups = int(userinput)
            self.dcups += add_cups
            self.setmainmenu()


coffee_machine = twogirls1cup(550, 400, 540, 120, 9)
while True:
    action = input()
    coffee_machine.evaluate(action)


# w = int(input("Write how many ml of water the coffee machine has:"))
# m = int(input("Write how many ml of milk the coffee machine has:"))
# c = int(input("Write how many grams of coffee beans the coffee machine has:"))
# cups = int(input("Write how many cups of coffee you will need:"))

# nw = w//200
# nm = m//50
# nc = c//15
# N = min(nw,nm,nc)
# if(cups<N):
#     print("Yes, I can make that amount of coffee (and even " + str(N - cups) + " more than that)")
# elif(cups==N):
#     print("Yes, I can make that amount of coffee")
# else:
#     print("No, I can make only " + str(N) + " cups of coffee")

# cups = int(input("Write how many cups of coffee you will need:"))
# print("For 125 cups of coffee you will need:")
# print(str(cups * 200) + " ml of water")
# print(str(cups * 50) + " ml of milk")
# print(str(cups * 15) + " g of coffee beans")

# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")