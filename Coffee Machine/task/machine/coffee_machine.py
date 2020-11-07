class CoffeeMachine(object):
    recipe_coffee = {
        "espresso": [250, 0, 16, 4],
        "latte": [350, 75, 20, 7],
        "cappuccino": [200, 100, 12, 6],
        }

    def __init__(self, level_water, level_milk, level_beans, level_disposable_cups, level_money):
        self.level_water = level_water
        self.level_milk = level_milk
        self.level_beans = level_beans
        self.level_disposable_cups = level_disposable_cups
        self.level_money = level_money

    def take_money(self):
        print(f"I gave you ${self.level_money}")
        self.level_money = 0

    def show_status(self):
        print(f"""
    The coffee machine has:
    {self.level_water} of water
    {self.level_milk} of milk
    {self.level_beans} of coffee beans
    {self.level_disposable_cups} of disposable cups
    {self.level_money} of money
        """)

    def make_coffee(self, water_used, milk_used, beans_used, money_used):
        self.level_water -= water_used
        self.level_milk -= milk_used
        self.level_beans -= beans_used
        self.level_disposable_cups -= 1
        self.level_money += money_used

    def check_can_make_coffee(self, water_used, milk_used, beans_used, money_used):
        check_passed = True
        missing_supply = ""
        if self.level_water - water_used < 0:
            missing_supply += "water"
            check_passed = False
        if self.level_milk - milk_used < 0:
            missing_supply += "milk"
            check_passed = False
        if self.level_beans - beans_used < 0:
            missing_supply += "milk"
            check_passed = False
        if self.level_disposable_cups - 1 < 0:
            missing_supply += "disposable cups"
            check_passed = False
        if check_passed:
            print("I have enough resources, making you a coffee!")
            self.make_coffee(water_used, milk_used, beans_used, money_used)
        else:
            print(f"Sorry, not enough {missing_supply}!")
        return check_passed

    def buy_coffee(self):
        needed_water, needed_milk, needed_beans, needed_money = 0, 0, 0, 0
        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if user_input == "1":
            needed_water, needed_milk, needed_beans, needed_money = CoffeeMachine.recipe_coffee["espresso"]
        elif user_input == "2":
            needed_water, needed_milk, needed_beans, needed_money = CoffeeMachine.recipe_coffee["latte"]
        elif user_input == "3":
            needed_water, needed_milk, needed_beans, needed_money = CoffeeMachine.recipe_coffee["cappuccino"]
        if user_input != "back":
            self.check_can_make_coffee(needed_water, needed_milk, needed_beans, needed_money)

    def fill_machine(self):
        user_number_water = int(input("Write how many ml of water do you want to add:"))
        user_number_milk = int(input("Write how many ml of milk do you want to add:"))
        user_number_beans = int(input("Write how many grams of coffee beans do you want to add:"))
        user_number_disposable_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.level_water = self.level_water + user_number_water
        self.level_milk = self.level_milk + user_number_milk
        self.level_beans = self.level_beans + user_number_beans
        self.level_disposable_cups = self.level_disposable_cups + user_number_disposable_cups

    def user_selection(self, user_selection):
        if user_selection == "buy":
            self.buy_coffee()
        elif user_selection == "fill":
            self.fill_machine()
        elif user_selection == "take":
            self.take_money()
        elif user_selection == "remaining":
            self.show_status()
        else:
            print("Error")


coffee_machina = CoffeeMachine(400, 540, 120, 9, 550)
user_choice = ""
while user_choice != "exit":
    user_choice = input("Write action (buy, fill, take, remaining, exit):")
    coffee_machina.user_selection(user_choice)
